import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path

st.set_page_config(
    page_title="Canadian Cosmetics Regulatory Compliance",
    page_icon="🧴",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .block-container{padding:1.5rem 2rem}
    .kpi{background:white;border-radius:12px;padding:16px 20px;border:1px solid #E8E8E8;box-shadow:0 1px 4px rgba(0,0,0,0.05);margin-bottom:8px}
    .kpi-label{font-size:11px;color:#888;margin-bottom:4px;font-weight:500;text-transform:uppercase;letter-spacing:.04em}
    .kpi-value{font-size:26px;font-weight:700;color:#111;line-height:1.1}
    .kpi-note{font-size:11px;color:#888;margin-top:3px}
    .kpi-red .kpi-value{color:#C0392B}
    .kpi-green .kpi-value{color:#0A7540}
    .kpi-amber .kpi-value{color:#B7791F}
    .kpi-blue .kpi-value{color:#0C447C}
    .finding{background:#F0FBF6;border-left:3px solid #27AE60;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#1A5C35;margin:10px 0;line-height:1.6}
    .alert{background:#FDF2F2;border-left:3px solid #C0392B;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#7B1818;margin:10px 0;line-height:1.6}
    .warning{background:#FEF9EC;border-left:3px solid #F39C12;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#7D5A00;margin:10px 0;line-height:1.6}
    .insight{background:#EEF3FB;border-left:3px solid #1A56DB;border-radius:0 8px 8px 0;padding:11px 15px;font-size:13px;color:#0C2A6E;margin:10px 0;line-height:1.6}
    .critical{background:#FDF2F2;border-left:4px solid #7B1818;padding:11px 15px;font-size:13px;color:#7B1818;margin:10px 0;line-height:1.6;font-weight:500;border-radius:0 8px 8px 0}
    .section-title{font-size:15px;font-weight:600;color:#111;margin:18px 0 10px 0;padding-bottom:6px;border-bottom:1.5px solid #EBEBEB}
    footer{visibility:hidden}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load():
    base = Path(__file__).parent
    reqs      = pd.read_csv(base / "regulatory-requirements.csv")
    products  = pd.read_csv(base / "product-audit.csv")
    claims    = pd.read_csv(base / "claims-analysis.csv")
    hotlist   = pd.read_csv(base / "hotlist-sample.csv")
    checklist = pd.read_csv(base / "pre-notification-checklist.csv")
    with open(base / "key-findings.json") as f:
        findings = json.load(f)
    return reqs, products, claims, hotlist, checklist, findings

reqs, products, claims, hotlist, checklist, findings = load()

SCORE_COLOR = lambda s: "#0A7540" if s>=80 else "#F59E0B" if s>=60 else "#C0392B"
RISK_COLORS = {"Critical":"#7B1818","High":"#C0392B","Medium":"#B7791F","Low to Medium":"#F59E0B","Low":"#0A7540"}

st.markdown("## Canadian Cosmetics Regulatory Compliance Analysis")
st.markdown("**8 regulatory requirements mapped** &nbsp;|&nbsp; **15 products audited** &nbsp;|&nbsp; **10 marketing claims assessed** &nbsp;|&nbsp; **10 Hotlist ingredients reviewed**")
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "  The Regulatory Landscape  ",
    "  Product Compliance Audit  ",
    "  The Claims Problem  ",
    "  Ingredient Hotlist  ",
    "  Pre-Launch Checklist  ",
])

# ── TAB 1 ─────────────────────────────────────────────────────────────────────
with tab1:
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Non-compliant products</div>
            <div class="kpi-value">{findings['non_compliant_products']} of {findings['products_audited']}</div>
            <div class="kpi-note">{findings['non_compliant_pct']}% of products audited</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="kpi kpi-red">
            <div class="kpi-label">Products with drug-like claims</div>
            <div class="kpi-value">{findings['products_with_drug_claims']}</div>
            <div class="kpi-note">Being sold as cosmetics — legally drugs</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="kpi kpi-amber">
            <div class="kpi-label">Missing notification</div>
            <div class="kpi-value">{findings['products_missing_notification']}</div>
            <div class="kpi-note">Health Canada not notified within 10 days</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class="kpi kpi-amber">
            <div class="kpi-label">Avg compliance score</div>
            <div class="kpi-value">{findings['avg_compliance_score']}/100</div>
            <div class="kpi-note">Across all 15 products audited</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="alert"><strong>The core finding:</strong> More than half of the products audited have at least one significant compliance gap. The most common is also the most serious — making claims that legally classify the product as a drug while selling it as a cosmetic with no drug approval. SPF products and products claiming to heal, repair, or stimulate hair growth are the most frequently misclassified.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">The eight regulatory requirements every Canadian cosmetics brand must meet</div>', unsafe_allow_html=True)
    for _, req in reqs.iterrows():
        box = "alert" if req["Category"] in ["Claims","Ingredient Safety"] else "warning" if req["Category"]=="Notification" else "insight"
        st.markdown(f"""<div class="{box}">
            <strong>{req['Req ID']} — {req['Requirement']}</strong><br>
            <strong>Regulatory reference:</strong> {req['Regulatory Reference']}<br>
            <strong>Most common gap:</strong> {req['Common Gap']}<br>
            <strong>Risk of non-compliance:</strong> {req['Risk of Non-Compliance']}
        </div>""", unsafe_allow_html=True)

# ── TAB 2 ─────────────────────────────────────────────────────────────────────
with tab2:
    st.markdown('<div class="section-title">Compliance scores across 15 fictional Canadian beauty products</div>', unsafe_allow_html=True)
    st.markdown('<div class="warning">Products scoring below 60 have at least one significant compliance gap. Products below 40 have critical issues requiring immediate action before the product can legally be sold in Canada.</div>', unsafe_allow_html=True)

    col1,col2 = st.columns(2)
    with col1:
        sorted_products = products.sort_values("Compliance Score", ascending=True)
        fig_scores = go.Figure(go.Bar(
            x=sorted_products["Compliance Score"],
            y=sorted_products["Product Name"],
            orientation="h",
            marker_color=[SCORE_COLOR(s) for s in sorted_products["Compliance Score"]],
            text=[f"{s}" for s in sorted_products["Compliance Score"]],
            textposition="outside",
        ))
        fig_scores.add_vline(x=60, line_dash="dot", line_color="#F59E0B", annotation_text="Min acceptable")
        fig_scores.add_vline(x=80, line_dash="dot", line_color="#0A7540", annotation_text="Target")
        fig_scores.update_layout(height=500, plot_bgcolor="white",
            xaxis=dict(title="Compliance Score", gridcolor="#F1F1F1", range=[0,115]),
            yaxis=dict(title="", tickfont=dict(size=10)),
            margin=dict(t=10,b=20))
        st.plotly_chart(fig_scores, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Compliance gaps by type</div>', unsafe_allow_html=True)
        gap_data = pd.DataFrame({
            "Gap Type": ["Drug-like claims","Missing notification","Missing bilingual label","No Hotlist check","No INCI format"],
            "Count":    [findings["products_with_drug_claims"], findings["products_missing_notification"],
                        findings["products_missing_bilingual"],
                        sum(1 for _,p in products.iterrows() if p["Hotlist Check Completed"]=="No"),
                        sum(1 for _,p in products.iterrows() if p["INCI Ingredient Format"]=="No")],
        })
        fig_gaps = go.Figure(go.Bar(
            x=gap_data["Count"], y=gap_data["Gap Type"],
            orientation="h",
            marker_color=["#7B1818","#C0392B","#F59E0B","#F59E0B","#F59E0B"],
            text=gap_data["Count"], textposition="outside",
        ))
        fig_gaps.update_layout(height=260, plot_bgcolor="white",
            xaxis=dict(title="Number of products", gridcolor="#F1F1F1"),
            yaxis=dict(title=""), margin=dict(t=10,b=20))
        st.plotly_chart(fig_gaps, use_container_width=True)

        st.markdown('<div class="section-title">Score distribution</div>', unsafe_allow_html=True)
        fig_dist = px.histogram(products, x="Compliance Score", nbins=10,
            color_discrete_sequence=["#4285F4"])
        fig_dist.add_vline(x=60, line_dash="dash", line_color="#C0392B")
        fig_dist.update_layout(height=220, plot_bgcolor="white",
            xaxis=dict(title="Compliance Score", gridcolor="#F1F1F1"),
            yaxis=dict(title="Products", gridcolor="#F1F1F1"),
            margin=dict(t=10,b=20))
        st.plotly_chart(fig_dist, use_container_width=True)

    st.markdown('<div class="section-title">Product detail — select a product to see its full compliance assessment</div>', unsafe_allow_html=True)
    selected = st.selectbox("Select product", products["Product Name"].tolist(), key="product_select")
    prod = products[products["Product Name"]==selected].iloc[0]
    score = prod["Compliance Score"]
    box = "finding" if score>=80 else "warning" if score>=60 else "alert"
    st.markdown(f"""<div class="{box}">
        <strong>{prod['Brand']} — {prod['Product Name']}</strong> &nbsp;|&nbsp; Compliance Score: {score}/100<br>
        <strong>Claims used:</strong> {prod['Claims Used']}<br>
        <strong>Drug-like claims present:</strong> {prod['Drug-Like Claims Present']}<br>
        <strong>Unsubstantiated claims:</strong> {prod['Unsubstantiated Marketing Claims']}<br>
        <strong>Key gap:</strong> {prod['Key Gap']}
    </div>""", unsafe_allow_html=True)

# ── TAB 3 ─────────────────────────────────────────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">Ten marketing terms assessed against Canadian regulations</div>', unsafe_allow_html=True)
    st.markdown('<div class="alert">Two terms — SPF and Heals or Repairs — are not unregulated marketing language. They are drug claims under Canadian law. Any product using these terms is legally a drug and cannot be sold without Health Canada drug approval. This is the most common and most serious compliance error in Canadian beauty retail.</div>', unsafe_allow_html=True)

    col1,col2 = st.columns(2)
    with col1:
        risk_counts = claims["Risk Level"].value_counts().reset_index()
        risk_counts.columns = ["Risk Level","Count"]
        fig_risk = px.pie(risk_counts, values="Count", names="Risk Level",
            color="Risk Level",
            color_discrete_map=RISK_COLORS, hole=0.45)
        fig_risk.update_layout(height=260, margin=dict(t=10,b=10))
        st.plotly_chart(fig_risk, use_container_width=True)

    with col2:
        usage = claims[["Claim Term","Products Using This Term","Risk Level"]].sort_values("Products Using This Term", ascending=True)
        fig_usage = px.bar(usage, x="Products Using This Term", y="Claim Term",
            orientation="h", color="Risk Level",
            color_discrete_map=RISK_COLORS, text="Products Using This Term")
        fig_usage.update_traces(textposition="outside")
        fig_usage.update_layout(height=300, plot_bgcolor="white",
            xaxis=dict(title="Products using this term", gridcolor="#F1F1F1"),
            yaxis=dict(title=""), margin=dict(t=10,b=20))
        st.plotly_chart(fig_usage, use_container_width=True)

    st.markdown('<div class="section-title">Claim-by-claim breakdown</div>', unsafe_allow_html=True)
    for _, claim in claims.iterrows():
        risk = claim["Risk Level"]
        box = "critical" if risk=="Critical" else "alert" if risk=="High" else "warning" if "Medium" in risk else "finding"
        st.markdown(f"""<div class="{box}">
            <strong>{claim['Claim Term']}</strong> — Risk: {risk} &nbsp;|&nbsp; Used on {claim['Products Using This Term']} products<br>
            <strong>What consumers think it means:</strong> {claim['What Consumers Think It Means']}<br>
            <strong>What Health Canada says:</strong> {claim['What Health Canada Says']}<br>
            <strong>Recommendation:</strong> {claim['Recommendation']}
        </div>""", unsafe_allow_html=True)

# ── TAB 4 ─────────────────────────────────────────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">Sample from the Health Canada Cosmetic Ingredient Hotlist</div>', unsafe_allow_html=True)
    st.markdown('<div class="insight">The Cosmetic Ingredient Hotlist is the most important reference document in Canadian cosmetics compliance. It is updated regularly and brands are responsible for staying current. An ingredient that was permitted last year may be restricted or prohibited today. The 10 entries below illustrate the range of restrictions — from outright prohibition to specific concentration limits by product type.</div>', unsafe_allow_html=True)

    status_filter = st.multiselect("Filter by status", hotlist["Status"].unique().tolist(),
        default=hotlist["Status"].unique().tolist(), key="hotlist_filter")
    filtered_hotlist = hotlist[hotlist["Status"].isin(status_filter)]

    col1,col2 = st.columns(2)
    with col1:
        status_counts = hotlist["Status"].value_counts().reset_index()
        status_counts.columns = ["Status","Count"]
        fig_status = px.pie(status_counts, values="Count", names="Status",
            color="Status",
            color_discrete_map={"Prohibited":"#C0392B","Restricted":"#F59E0B"},
            hole=0.45)
        fig_status.update_layout(height=240, margin=dict(t=10,b=10))
        st.plotly_chart(fig_status, use_container_width=True)

    with col2:
        st.markdown('<div class="section-title">Commonly found in products</div>', unsafe_allow_html=True)
        st.dataframe(filtered_hotlist[["Ingredient INCI Name","Status","Commonly Found In","Consumer Risk"]],
            use_container_width=True, hide_index=True)

    st.markdown('<div class="section-title">Full Hotlist sample</div>', unsafe_allow_html=True)
    for _, ing in filtered_hotlist.iterrows():
        box = "alert" if ing["Status"]=="Prohibited" else "warning"
        st.markdown(f"""<div class="{box}">
            <strong>{ing['Ingredient INCI Name']}</strong> — {ing['Status']}<br>
            <strong>Restriction:</strong> {ing['Restriction']}<br>
            <strong>Consumer risk:</strong> {ing['Consumer Risk']}
        </div>""", unsafe_allow_html=True)

# ── TAB 5 ─────────────────────────────────────────────────────────────────────
with tab5:
    st.markdown('<div class="section-title">Pre-launch compliance checklist for a new cosmetic product in Canada</div>', unsafe_allow_html=True)
    st.markdown('<div class="finding">Ten steps a regulatory affairs analyst would complete before a new cosmetic product can legally be sold in Canada. Steps 1 through 7 should be completed before launch. Step 8 must be completed within 10 days of first sale. Steps 9 and 10 are ongoing after launch.</div>', unsafe_allow_html=True)

    phase_filter = st.multiselect("Filter by phase",
        checklist["Phase"].unique().tolist(),
        default=checklist["Phase"].unique().tolist(), key="checklist_filter")
    filtered_checklist = checklist[checklist["Phase"].isin(phase_filter)]

    for _, step in filtered_checklist.iterrows():
        box = "alert" if step["Phase"]=="Notification" else "warning" if step["Phase"]=="Formulation Review" else "insight" if step["Phase"]=="Post-Launch" else "finding"
        st.markdown(f"""<div class="{box}">
            <strong>Step {int(step['Step'])} — {step['Phase']}: {step['Task']}</strong><br>
            <strong>Why this matters:</strong> {step['Why This Matters']}<br>
            <strong>Who is responsible:</strong> {step['Responsible']} &nbsp;|&nbsp; <strong>Typical timeline:</strong> {step['Typical Timeline']}<br>
            <strong>Documentation required:</strong> {step['Required Documentation']}
        </div>""", unsafe_allow_html=True)

st.divider()
st.markdown(
    "**Regulatory note:** All regulatory information is based on Health Canada Cosmetics Regulations "
    "and the Cosmetic Ingredient Hotlist as of May 2026. Regulations change regularly — always verify "
    "current requirements directly with Health Canada before making compliance decisions. "
    "All brand names and products are fictional. "
    "Prepared by Simran Saran as part of The Case Files portfolio series."
)
