import csv
import json
import random

random.seed(55)

# Canadian Cosmetics Regulatory Compliance Analysis
# Based on Health Canada Cosmetics Regulations under the Food and Drugs Act
# Cosmetic Ingredient Hotlist and labelling requirements
# May 2026

# ── REGULATORY REQUIREMENTS ───────────────────────────────────────────────────
requirements = [
    {
        "Req ID": "COS-001",
        "Category": "Notification",
        "Requirement": "A company must notify Health Canada within 10 days of first selling a cosmetic product in Canada. This applies to every product in every format including online sales.",
        "Regulatory Reference": "Cosmetics Regulations Section 30",
        "Who It Applies To": "All cosmetic manufacturers and importers selling in Canada",
        "How To Comply": "Submit a cosmetic notification form through the Health Canada online portal including product name, company details, and ingredient list",
        "Common Gap": "Small and indie brands frequently miss this requirement when launching online. Many are unaware it exists.",
        "Risk of Non-Compliance": "Product seizure and market withdrawal. Up to $5,000 fine per violation.",
    },
    {
        "Req ID": "COS-002",
        "Category": "Labelling",
        "Requirement": "All cosmetic labels must be bilingual in English and French. Every required element must appear in both official languages.",
        "Regulatory Reference": "Consumer Packaging and Labelling Act and Cosmetics Regulations Section 21",
        "Who It Applies To": "All cosmetic products sold in Canada",
        "How To Comply": "Ensure product name, net quantity, company name and address, and directions for use all appear in both English and French",
        "Common Gap": "Brands entering Canada from the US or UK frequently launch with English-only labels. French is not optional.",
        "Risk of Non-Compliance": "Product cannot legally be sold in Canada. Can be removed from shelves by inspectors.",
    },
    {
        "Req ID": "COS-003",
        "Category": "Labelling",
        "Requirement": "All ingredients must be listed on the label in descending order of concentration using International Nomenclature of Cosmetic Ingredients (INCI) names",
        "Regulatory Reference": "Cosmetics Regulations Section 22",
        "Who It Applies To": "All cosmetic products sold in Canada",
        "How To Comply": "Use the official INCI name for every ingredient. List from highest to lowest concentration. Ingredients below 1% concentration may be listed in any order.",
        "Common Gap": "Using common names or trade names instead of INCI names. Missing ingredients added during manufacturing. Wrong order of listing.",
        "Risk of Non-Compliance": "Product labelling violation. Potential market withdrawal.",
    },
    {
        "Req ID": "COS-004",
        "Category": "Ingredient Safety",
        "Requirement": "No product may contain any ingredient listed as prohibited on the Health Canada Cosmetic Ingredient Hotlist",
        "Regulatory Reference": "Food and Drugs Act Section 16 and Cosmetic Ingredient Hotlist",
        "Who It Applies To": "All cosmetic products sold in Canada",
        "How To Comply": "Review every ingredient against the current Hotlist before formulating or importing. Update formulations if an ingredient is added to the Hotlist after launch.",
        "Common Gap": "Brands formulating outside Canada frequently do not check the Canadian Hotlist. EU or US formulations may include ingredients prohibited in Canada.",
        "Risk of Non-Compliance": "Criminal prosecution under the Food and Drugs Act. Product recall and market withdrawal.",
    },
    {
        "Req ID": "COS-005",
        "Category": "Ingredient Safety",
        "Requirement": "Restricted ingredients listed on the Hotlist may only be used within their specified concentration limits and in the product types permitted",
        "Regulatory Reference": "Cosmetic Ingredient Hotlist — Restricted Substances",
        "Who It Applies To": "Any product containing a restricted ingredient",
        "How To Comply": "Confirm concentration levels in formulation documentation. Do not use restricted ingredient in product types where it is not permitted even if within concentration limits.",
        "Common Gap": "A preservative permitted in rinse-off products at a certain concentration is sometimes used in leave-on products where a lower limit or complete restriction applies.",
        "Risk of Non-Compliance": "Same as prohibited ingredient violation — potential prosecution and recall.",
    },
    {
        "Req ID": "COS-006",
        "Category": "Claims",
        "Requirement": "A cosmetic product must not make claims that suggest it treats, prevents, or cures a disease or condition. Products making such claims are classified as drugs not cosmetics and require drug approval.",
        "Regulatory Reference": "Food and Drugs Act — Definition of Drug vs Cosmetic",
        "Who It Applies To": "All cosmetic products",
        "How To Comply": "Ensure marketing language stays within cosmetic claim territory — alters appearance, cleanses, perfumes. Remove any claim that implies a physiological effect or disease treatment.",
        "Common Gap": "Anti-aging products frequently drift into drug territory with claims like repairs DNA damage or stimulates collagen production. Sunscreens making SPF claims are classified as drugs in Canada and require drug approval not cosmetic notification.",
        "Risk of Non-Compliance": "Product classified as unapproved drug. Criminal prosecution possible. Mandatory market withdrawal.",
    },
    {
        "Req ID": "COS-007",
        "Category": "Claims",
        "Requirement": "Terms like natural, clean, organic, non-toxic, and hypoallergenic have no legal definition under Canadian cosmetics law. Companies using these terms bear responsibility for being able to substantiate them if challenged.",
        "Regulatory Reference": "Food and Drugs Act — Misleading Representations and Health Canada Guidance on Cosmetic Claims",
        "Who It Applies To": "Any product using unregulated marketing claims",
        "How To Comply": "Maintain internal documentation substantiating any claim made on the label or in marketing. Certify organic claims through an accredited certifier. Be able to define what natural or clean means for your product specifically.",
        "Common Gap": "Most brands use these terms as marketing language without any internal definition or substantiation file. If Health Canada or a competitor challenges the claim the company has nothing to defend it with.",
        "Risk of Non-Compliance": "Misleading advertising complaint. Competition Bureau investigation. Consumer trust damage.",
    },
    {
        "Req ID": "COS-008",
        "Category": "Labelling",
        "Requirement": "The name and address of the company responsible for the product must appear on the label — either the Canadian manufacturer or the importer",
        "Regulatory Reference": "Cosmetics Regulations Section 21(c)",
        "Who It Applies To": "All cosmetic products sold in Canada",
        "How To Comply": "If the product is manufactured outside Canada the Canadian importer's name and address must appear on the label. A foreign manufacturer's address alone is not sufficient.",
        "Common Gap": "Products imported directly and resold without a Canadian entity listed on the label. Common with dropshipping and direct-to-consumer international brands.",
        "Risk of Non-Compliance": "Labelling violation. Cannot legally be sold in Canada.",
    },
]

with open('/home/claude/cosmetics-compliance/regulatory-requirements.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=requirements[0].keys())
    w.writeheader(); w.writerows(requirements)

print(f"Regulatory requirements: {len(requirements)}")

# ── PRODUCT COMPLIANCE AUDIT ─────────────────────────────────────────────────
products = [
    {"Product ID":"PRD-001","Brand":"Lumière Naturals","Product Name":"Radiance Boost Serum","Category":"Serum","Claims Used":"Clean beauty. 97% natural origin. Clinically proven to reduce fine lines in 4 weeks.","Bilingual Label":"No","INCI Ingredient Format":"Yes","Health Canada Notification":"No","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"Yes — clinically proven to reduce fine lines implies physiological effect","Unsubstantiated Marketing Claims":"Clean beauty. 97% natural origin — no certification","Compliance Score":32,"Key Gap":"Missing bilingual labelling. No Health Canada notification. Drug-like claims require reclassification."},
    {"Product ID":"PRD-002","Brand":"PureRoots","Product Name":"Hydrating Face Cream","Category":"Moisturizer","Claims Used":"Non-toxic. Free from parabens, sulfates, phthalates. Dermatologist tested.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"No","Unsubstantiated Marketing Claims":"Non-toxic — no legal definition. Dermatologist tested — no standard for this term.","Compliance Score":74,"Key Gap":"Unsubstantiated claims with no internal documentation. Otherwise well-compliant."},
    {"Product ID":"PRD-003","Brand":"GlowLab","Product Name":"SPF 30 Daily Moisturizer","Category":"Sunscreen","Claims Used":"Broad spectrum SPF 30. Protects against UV damage. Lightweight formula.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"Yes — SPF products are classified as drugs in Canada not cosmetics","Unsubstantiated Marketing Claims":"None beyond SPF claim","Compliance Score":25,"Key Gap":"Critical: SPF claims make this product a drug under Canadian law. Requires Drug Identification Number — not cosmetic notification."},
    {"Product ID":"PRD-004","Brand":"Botanica Co.","Product Name":"Curl Defining Cream","Category":"Hair Care","Claims Used":"100% natural. Vegan. Cruelty-free.","Bilingual Label":"Yes","INCI Ingredient Format":"No — uses common names not INCI","Health Canada Notification":"Yes","Hotlist Check Completed":"No","Prohibited Ingredients Found":"Unknown — not checked","Restricted Ingredients in Limits":"Unknown","Drug-Like Claims Present":"No","Unsubstantiated Marketing Claims":"100% natural — no certification. Cruelty-free — no accredited certification.","Compliance Score":48,"Key Gap":"Ingredient list uses common names not INCI. Hotlist check not completed. Natural and cruelty-free claims unsubstantiated."},
    {"Product ID":"PRD-005","Brand":"Maison Claire","Product Name":"Brightening Eye Cream","Category":"Eye Cream","Claims Used":"Clinically tested. Reduces dark circles by 78% in 2 weeks. Ophthalmologist approved.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"No","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"Yes — reduces dark circles by 78% and clinically tested imply physiological drug effect","Unsubstantiated Marketing Claims":"Ophthalmologist approved — no standard exists for this term","Compliance Score":28,"Key Gap":"Drug-like efficacy claims. No Health Canada notification. Ophthalmologist approved is a meaningless unregulated term."},
    {"Product ID":"PRD-006","Brand":"NorthGlow","Product Name":"Vitamin C Brightening Serum","Category":"Serum","Claims Used":"Brightens skin tone. Antioxidant protection. Made with 15% Vitamin C.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"No — brightening is cosmetic claim territory","Unsubstantiated Marketing Claims":"Minor — antioxidant protection is borderline but defensible","Compliance Score":88,"Key Gap":"Minor claim clarification recommended. Otherwise strong compliance."},
    {"Product ID":"PRD-007","Brand":"TerraBotanica","Product Name":"Charcoal Detox Cleanser","Category":"Cleanser","Claims Used":"Detoxifies pores. Removes toxins. Deep clean for healthier skin.","Bilingual Label":"No","INCI Ingredient Format":"Yes","Health Canada Notification":"No","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"Yes — removes toxins and detoxifies imply physiological action","Unsubstantiated Marketing Claims":"Detoxifies — no scientific basis. Removes toxins — skin does not accumulate toxins in the way claimed.","Compliance Score":22,"Key Gap":"Missing bilingual labelling. No notification. Detox and toxin removal claims are misleading and possibly drug claims."},
    {"Product ID":"PRD-008","Brand":"Soleil Skin","Product Name":"Gentle Daily Moisturizer","Category":"Moisturizer","Claims Used":"Hydrates and softens skin. Suitable for sensitive skin. Fragrance-free.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"No","Unsubstantiated Marketing Claims":"Suitable for sensitive skin — no dermatological standard but low risk","Compliance Score":92,"Key Gap":"No significant gaps. Best-in-class compliance among products audited."},
    {"Product ID":"PRD-009","Brand":"WildRoots Beauty","Product Name":"Organic Rosehip Face Oil","Category":"Face Oil","Claims Used":"Certified organic. Heals scars. Reverses signs of aging.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"Yes — heals scars is a drug claim","Unsubstantiated Marketing Claims":"Reverses signs of aging — drug territory. Certified organic — check if certification is from accredited body.","Compliance Score":41,"Key Gap":"Heals scars is a drug claim requiring reclassification. Reverses aging is borderline. Organic certification must be verified."},
    {"Product ID":"PRD-010","Brand":"CleanSlate Lab","Product Name":"AHA Exfoliating Toner","Category":"Toner","Claims Used":"Clean formula. Exfoliates dead skin. Resurfaces skin texture.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes — AHA at compliant concentration","Drug-Like Claims Present":"No — exfoliation is cosmetic territory","Unsubstantiated Marketing Claims":"Clean formula — no definition provided","Compliance Score":79,"Key Gap":"Clean formula claim needs internal substantiation file. Otherwise compliant."},
    {"Product ID":"PRD-011","Brand":"Velour Cosmetics","Product Name":"Long-Wear Lipstick","Category":"Lip Product","Claims Used":"Transfer-proof. 16-hour wear. Safe for sensitive lips.","Bilingual Label":"Yes","INCI Ingredient Format":"No — trade names used for several colourants","Health Canada Notification":"Yes","Hotlist Check Completed":"No","Prohibited Ingredients Found":"Unknown — colourant Hotlist check not completed","Restricted Ingredients in Limits":"Unknown","Drug-Like Claims Present":"No","Unsubstantiated Marketing Claims":"16-hour wear — performance claim, low risk if tested","Compliance Score":51,"Key Gap":"Colourants must be individually checked against the Hotlist. INCI names required for all colourants."},
    {"Product ID":"PRD-012","Brand":"Arctic Botanics","Product Name":"Scalp Treatment Oil","Category":"Hair Care","Claims Used":"Stimulates hair growth. Clinically shown to reduce hair loss by 40%.","Bilingual Label":"No","INCI Ingredient Format":"Yes","Health Canada Notification":"No","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"Yes — stimulates hair growth and reduces hair loss are drug claims","Unsubstantiated Marketing Claims":"Clinically shown — no study referenced or methodology disclosed","Compliance Score":14,"Key Gap":"Critical non-compliance. Hair growth and hair loss claims make this an unapproved drug. Requires Drug Identification Number process."},
    {"Product ID":"PRD-013","Brand":"Marigold Skin","Product Name":"Calming Redness Serum","Category":"Serum","Claims Used":"Calms redness and irritation. Soothes sensitive skin. Gentle formula.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"No — calming and soothing are cosmetic claims","Unsubstantiated Marketing Claims":"None significant","Compliance Score":90,"Key Gap":"Well-compliant. Minor recommendation to document claim substantiation for soothing claim."},
    {"Product ID":"PRD-014","Brand":"Ember Beauty","Product Name":"Firming Body Lotion","Category":"Body Care","Claims Used":"Firms and tones skin. Reduces appearance of cellulite. Non-toxic ingredients.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"No — reduces appearance of is cosmetic territory","Unsubstantiated Marketing Claims":"Firms and tones — cosmetic claim requiring substantiation file. Non-toxic — no legal definition.","Compliance Score":68,"Key Gap":"Claim substantiation documentation missing. Non-toxic needs internal definition."},
    {"Product ID":"PRD-015","Brand":"PurePath","Product Name":"Micellar Cleansing Water","Category":"Cleanser","Claims Used":"Removes makeup gently. No rinsing required. Suitable for all skin types.","Bilingual Label":"Yes","INCI Ingredient Format":"Yes","Health Canada Notification":"Yes","Hotlist Check Completed":"Yes","Prohibited Ingredients Found":"No","Restricted Ingredients in Limits":"Yes","Drug-Like Claims Present":"No","Unsubstantiated Marketing Claims":"Suitable for all skin types — low risk claim","Compliance Score":94,"Key Gap":"No significant gaps. Minor documentation recommendation only."},
]

with open('/home/claude/cosmetics-compliance/product-audit.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=products[0].keys())
    w.writeheader(); w.writerows(products)

print(f"Product audit: {len(products)} products")

# ── CLAIMS ANALYSIS ───────────────────────────────────────────────────────────
claims = [
    {"Claim Term":"Clean","What Consumers Think It Means":"Free from harmful or toxic ingredients","What Health Canada Says":"No legal definition. Term is entirely unregulated.","Is It Regulated in Canada":"No","Products Using This Term": 4,"Risk Level":"Medium","Why It Matters":"Without a standard any product can call itself clean. Consumers make purchasing decisions based on a term that means nothing legally.","Recommendation":"Maintain an internal definition document. List specifically what the product does not contain."},
    {"Claim Term":"Natural","What Consumers Think It Means":"Made from plant or earth-derived ingredients only","What Health Canada Says":"No legal definition. No minimum percentage of natural ingredients is required.","Is It Regulated in Canada":"No","Products Using This Term": 3,"Risk Level":"Medium","Why It Matters":"A product can be 5% plant-derived and call itself natural. The term is used across price points with completely different meanings.","Recommendation":"Define what natural means for your brand in an internal policy. Consider third-party certification."},
    {"Claim Term":"Non-Toxic","What Consumers Think It Means":"Contains no toxic or dangerous ingredients","What Health Canada Says":"No legal definition. All cosmetics already must not contain prohibited ingredients so the claim is either redundant or misleading.","Is It Regulated in Canada":"No","Products Using This Term": 3,"Risk Level":"Medium","Why It Matters":"The word toxic is a scientific term with a specific meaning. Using it as marketing language without definition is potentially misleading.","Recommendation":"Replace with specific claims about what is not included. Being free from parabens is more defensible than non-toxic."},
    {"Claim Term":"Clinically Proven","What Consumers Think It Means":"Tested in a clinical trial with documented results","What Health Canada Says":"No standard for what constitutes a clinical test in cosmetics. The claim can be used after a consumer perception study of 20 people.","Is It Regulated in Canada":"Partially — cannot make drug-like efficacy claims","Products Using This Term": 3,"Risk Level":"High","Why It Matters":"Consumers assume clinical means pharmaceutical-grade evidence. Most cosmetic clinical tests are far below that standard and the methodology is almost never disclosed.","Recommendation":"Specify the study type and sample size if using this claim. Avoid if the evidence is a perception survey only."},
    {"Claim Term":"Dermatologist Tested","What Consumers Think It Means":"Reviewed and approved by a dermatologist","What Health Canada Says":"No standard exists. One dermatologist testing one product constitutes compliance with the literal claim.","Is It Regulated in Canada":"No","Products Using This Term": 2,"Risk Level":"Medium","Why It Matters":"The claim implies expert medical endorsement with no defined standard behind it.","Recommendation":"Specify what the dermatologist tested for. Retain the testing documentation."},
    {"Claim Term":"Organic","What Consumers Think It Means":"Certified to meet organic production standards","What Health Canada Says":"No federal standard for organic cosmetics. Companies may use certification bodies but it is not mandatory.","Is It Regulated in Canada":"No federal standard — provincial and third-party certifications exist","Products Using This Term": 2,"Risk Level":"High","Why It Matters":"Organic on food has a legal meaning. Organic on cosmetics does not. Consumers apply the same assumption to both.","Recommendation":"Use only if certified by an accredited body such as ECOCERT or COSMOS. Display the certification mark prominently."},
    {"Claim Term":"Cruelty-Free","What Consumers Think It Means":"No animal testing at any stage of production","What Health Canada Says":"No legal standard in Canada for this claim.","Is It Regulated in Canada":"No","Products Using This Term": 2,"Risk Level":"Low to Medium","Why It Matters":"A brand can call itself cruelty-free while using contract manufacturers that test on animals. Without third-party certification the claim is unverifiable.","Recommendation":"Obtain Leaping Bunny or PETA certification. Display the certification mark to make the claim credible."},
    {"Claim Term":"Heals or Repairs","What Consumers Think It Means":"Fixes skin damage or repairs the skin barrier","What Health Canada Says":"Heal and repair are drug claims in Canada. Products making these claims require Drug Identification Number approval not cosmetic notification.","Is It Regulated in Canada":"Yes — these are drug claims","Products Using This Term": 2,"Risk Level":"Critical","Why It Matters":"Any product claiming to heal skin is legally a drug in Canada. Selling it as a cosmetic is a violation of the Food and Drugs Act.","Recommendation":"Remove immediately. Replace with cosmetically appropriate language such as helps improve the appearance of dry or damaged skin."},
    {"Claim Term":"Detoxifies or Removes Toxins","What Consumers Think It Means":"Removes harmful substances from the skin","What Health Canada Says":"The skin does not accumulate toxins in the way this claim implies. The claim may be considered misleading.","Is It Regulated in Canada":"No specific standard but misleading claims are prohibited","Products Using This Term": 1,"Risk Level":"High","Why It Matters":"The claim has no scientific basis in the context of topical cosmetics and may constitute a misleading representation under the Competition Act.","Recommendation":"Remove. Replace with deep cleansing or purifying which are cosmetically appropriate."},
    {"Claim Term":"SPF or Sun Protection","What Consumers Think It Means":"Product protects against UV damage","What Health Canada Says":"SPF claims make a product a drug in Canada not a cosmetic. The product requires Drug Identification Number approval.","Is It Regulated in Canada":"Yes — SPF products are drugs","Products Using This Term": 1,"Risk Level":"Critical","Why It Matters":"This is one of the most commonly misclassified product types in Canadian beauty. Many moisturizers with SPF are sold as cosmetics when they legally require drug approval.","Recommendation":"Pursue Drug Identification Number through Health Canada. Do not sell as a cosmetic."},
]

with open('/home/claude/cosmetics-compliance/claims-analysis.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=claims[0].keys())
    w.writeheader(); w.writerows(claims)

print(f"Claims analysis: {len(claims)} claim terms")

# ── HOTLIST INGREDIENT SAMPLE ─────────────────────────────────────────────────
hotlist = [
    {"Ingredient INCI Name":"Mercury and mercury compounds","CAS Number":"7439-97-6","Status":"Prohibited","Restriction":"Not permitted in any cosmetic product","Commonly Found In":"Some skin-lightening products. Imported products from certain markets.","Consumer Risk":"Neurotoxic. Kidney damage with prolonged exposure."},
    {"Ingredient INCI Name":"Formaldehyde","CAS Number":"50-00-0","Status":"Restricted","Restriction":"Maximum 0.2% as preservative. Not permitted in aerosols. Must include warning label if above 0.05%.","Commonly Found In":"Some nail polishes, hair straightening treatments, preservative systems","Consumer Risk":"Skin sensitizer. Potential carcinogen at higher concentrations."},
    {"Ingredient INCI Name":"Triclosan","CAS Number":"3380-34-5","Status":"Restricted","Restriction":"Maximum 0.3% in toothpaste and facial products. 0.2% in deodorants. 0.1% in other rinse-off products. Prohibited in leave-on body products.","Commonly Found In":"Some antibacterial cleansers and toothpastes","Consumer Risk":"Endocrine disruption concerns. Contributes to antibiotic resistance."},
    {"Ingredient INCI Name":"Dibutyl Phthalate (DBP)","CAS Number":"84-74-2","Status":"Restricted","Restriction":"Not permitted in cosmetics sold in Canada. Prohibited.","Commonly Found In":"Some nail polishes manufactured outside Canada","Consumer Risk":"Endocrine disruptor. Developmental toxicity concerns."},
    {"Ingredient INCI Name":"Hydroquinone","CAS Number":"123-31-9","Status":"Restricted","Restriction":"Not permitted in cosmetics. Permitted only in nail products up to 0.02% as polymerisation inhibitor.","Commonly Found In":"Some skin-lightening and brightening serums","Consumer Risk":"Potential carcinogen with prolonged use. Skin sensitizer."},
    {"Ingredient INCI Name":"Resorcinol","CAS Number":"108-46-3","Status":"Restricted","Restriction":"Maximum 0.5% in hair dyes. Prohibited in other cosmetic products. Warning label required.","Commonly Found In":"Hair colour products","Consumer Risk":"Skin sensitizer. Thyroid disruption concerns at high exposures."},
    {"Ingredient INCI Name":"Boric Acid","CAS Number":"10043-35-3","Status":"Restricted","Restriction":"Not permitted in products for children under 3. Maximum 0.1% in other products except bath salts where higher levels are permitted.","Commonly Found In":"Some baby products. Eye drops. Bath products.","Consumer Risk":"Developmental toxicity. Reproductive toxicity concerns."},
    {"Ingredient INCI Name":"Chloroform","CAS Number":"67-66-3","Status":"Prohibited","Restriction":"Not permitted in any cosmetic product in any concentration.","Commonly Found In":"Historical use as solvent. No legitimate current cosmetic use.","Consumer Risk":"Hepatotoxic. Potential carcinogen."},
    {"Ingredient INCI Name":"Methylene Glycol","CAS Number":"463-57-0","Status":"Restricted","Restriction":"Not permitted in hair smoothing products applied with heat above regulatory limits.","Commonly Found In":"Brazilian blowout and keratin hair treatment products","Consumer Risk":"Releases formaldehyde when heated. Respiratory sensitizer."},
    {"Ingredient INCI Name":"Lead and lead compounds","CAS Number":"7439-92-1","Status":"Prohibited","Restriction":"Not permitted in cosmetics as an intentionally added ingredient. Trace contamination limits apply.","Commonly Found In":"Some colour cosmetics from unregulated markets","Consumer Risk":"Neurotoxin. Developmental toxicity. No safe level of exposure."},
]

with open('/home/claude/cosmetics-compliance/hotlist-sample.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=hotlist[0].keys())
    w.writeheader(); w.writerows(hotlist)

print(f"Hotlist sample: {len(hotlist)} ingredients")

# ── PRE-NOTIFICATION CHECKLIST ────────────────────────────────────────────────
checklist = [
    {"Step":1,"Phase":"Formulation Review","Task":"Review every ingredient in the formulation against the current Health Canada Cosmetic Ingredient Hotlist","Why This Matters":"Prohibited ingredients cannot be sold in Canada regardless of what is permitted in other markets","Responsible":"Regulatory Affairs or Formulation Team","Typical Timeline":"1 to 2 weeks","Required Documentation":"Ingredient review sign-off. Hotlist check record."},
    {"Step":2,"Phase":"Formulation Review","Task":"Confirm restricted ingredients are within their permitted concentration limits for the specific product type","Why This Matters":"An ingredient permitted in a rinse-off product may be prohibited or at a lower limit in a leave-on product","Responsible":"Regulatory Affairs or Formulation Team","Typical Timeline":"Concurrent with Step 1","Required Documentation":"Formulation specification with concentrations. Restriction compliance record."},
    {"Step":3,"Phase":"Product Classification","Task":"Confirm the product is classified as a cosmetic not a drug or natural health product","Why This Matters":"SPF claims, hair growth claims, healing claims and others trigger drug classification. Wrong classification leads to selling an unapproved drug.","Responsible":"Regulatory Affairs","Typical Timeline":"1 week","Required Documentation":"Classification rationale document. Claims review."},
    {"Step":4,"Phase":"Claims Review","Task":"Review all label and marketing claims against Health Canada guidance on acceptable cosmetic claims","Why This Matters":"Drug-like claims require reclassification. Misleading unsubstantiated claims create regulatory and legal risk.","Responsible":"Regulatory Affairs and Marketing","Typical Timeline":"1 week","Required Documentation":"Claims review record. Substantiation files for each claim used."},
    {"Step":5,"Phase":"Label Review","Task":"Confirm label includes all required elements in both English and French","Why This Matters":"Bilingual labelling is mandatory in Canada. Missing elements prevent legal sale.","Responsible":"Regulatory Affairs or Compliance","Typical Timeline":"3 to 5 days","Required Documentation":"Label review checklist. Approved label artwork."},
    {"Step":6,"Phase":"Label Review","Task":"Confirm all ingredients are listed in descending concentration order using correct INCI names","Why This Matters":"INCI names are required by regulation. Common or trade names are not acceptable.","Responsible":"Regulatory Affairs or Formulation Team","Typical Timeline":"3 to 5 days","Required Documentation":"INCI ingredient list verified against formulation specification."},
    {"Step":7,"Phase":"Label Review","Task":"Confirm Canadian importer or manufacturer name and address appears on the label","Why This Matters":"A foreign manufacturer address alone does not satisfy Canadian labelling requirements","Responsible":"Regulatory Affairs","Typical Timeline":"1 to 2 days","Required Documentation":"Label review checklist."},
    {"Step":8,"Phase":"Notification","Task":"Submit Health Canada cosmetic notification form through the online portal within 10 days of first sale in Canada","Why This Matters":"Notification is legally required. Late submission is a violation even if the product is otherwise compliant.","Responsible":"Regulatory Affairs","Typical Timeline":"Submit before or within 10 days of first sale","Required Documentation":"Completed notification form. Confirmation from Health Canada portal."},
    {"Step":9,"Phase":"Post-Launch","Task":"Monitor Health Canada updates to the Cosmetic Ingredient Hotlist and re-assess formulation if new restrictions are added","Why This Matters":"Ingredients can be added to the Hotlist after a product launches. Companies are responsible for maintaining compliance ongoing.","Responsible":"Regulatory Affairs","Typical Timeline":"Ongoing — review Hotlist quarterly","Required Documentation":"Quarterly Hotlist review record. Formulation update record if required."},
    {"Step":10,"Phase":"Post-Launch","Task":"Maintain claim substantiation files for any claim used on the label or in marketing materials","Why This Matters":"Health Canada or a competitor can challenge a claim at any time. Companies without substantiation files have no defence.","Responsible":"Regulatory Affairs and Marketing","Typical Timeline":"Ongoing","Required Documentation":"Substantiation file for each active claim. Updated when claims change."},
]

with open('/home/claude/cosmetics-compliance/pre-notification-checklist.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=checklist[0].keys())
    w.writeheader(); w.writerows(checklist)

print(f"Pre-notification checklist: {len(checklist)} steps")

# Key findings
non_compliant = sum(1 for p in products if p["Compliance Score"] < 60)
drug_claims = sum(1 for p in products if p["Drug-Like Claims Present"] != "No")
no_notification = sum(1 for p in products if p["Health Canada Notification"] == "No")
no_bilingual = sum(1 for p in products if p["Bilingual Label"] == "No")
avg_score = round(sum(p["Compliance Score"] for p in products) / len(products), 1)
critical_claims = sum(1 for c in claims if c["Risk Level"] == "Critical")

findings = {
    "products_audited": len(products),
    "non_compliant_products": non_compliant,
    "non_compliant_pct": round(non_compliant/len(products)*100,1),
    "products_with_drug_claims": drug_claims,
    "products_missing_notification": no_notification,
    "products_missing_bilingual": no_bilingual,
    "avg_compliance_score": avg_score,
    "claims_analysed": len(claims),
    "critical_risk_claims": critical_claims,
    "hotlist_ingredients_reviewed": len(hotlist),
    "checklist_steps": len(checklist),
    "regulatory_requirements_mapped": len(requirements),
    "most_common_gap": "Drug-like claims requiring product reclassification",
    "best_compliant_product": "PurePath Micellar Cleansing Water (94)",
    "least_compliant_product": "Arctic Botanics Scalp Treatment Oil (14)",
}

with open('/home/claude/cosmetics-compliance/key-findings.json', 'w') as f:
    json.dump(findings, f, indent=2)

print(f"\nKey findings:")
print(f"  Non-compliant products: {non_compliant} of {len(products)} ({findings['non_compliant_pct']}%)")
print(f"  Products with drug-like claims: {drug_claims}")
print(f"  Missing Health Canada notification: {no_notification}")
print(f"  Missing bilingual labelling: {no_bilingual}")
print(f"  Average compliance score: {avg_score}/100")
print("All files written.")
