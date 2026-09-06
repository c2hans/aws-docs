---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/nist-sp-800-171-rev-3-transition.html
---

# NIST SP 800-171 Rev 3 transition
<a name="nist-sp-800-171-rev-3-transition"></a>

CMMC Level 2 currently assesses against NIST SP 800-171 Rev 2. However, NIST published [SP 800-171 Revision 3](https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final) in May 2024, and the DoD published mandatory [Organization-Defined Parameters (ODPs) for Rev 3](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://dodcio.defense.gov/Portals/0/Documents/CMMC/OrgDefinedParmsNISTSP800-171.pdf&ved=2ahUKEwjH96LcmfaTAxVmEFkFHRCGCzcQFnoECBcQAQ&usg=AOvVaw3v8ObcYK5D5FSYLgX1VUGk) in April 2025. While the DoD has not yet amended 32 CFR Part 170 to incorporate Rev 3, and the transition timeline is not publicly defined, organizations should be aware of the coming changes.

## Key changes in Rev 3
<a name="key-changes-in-rev-3"></a>
+ Two new control families are added: Planning (PL) and Supply Chain Risk Management (SR).
+ Rev 3 introduces ODPs across 50 of its 97 controls, requiring organizations to define specific values for frequencies, time periods, event types, and thresholds. The DoD has published mandatory values for all ODPs.
+ Of the 124 mapped requirements between Rev 2 and Rev 3, 47 gained new ODPs, 46 had significant language changes, 33 were withdrawn (consolidated or removed), 13 are entirely new with no Rev 2 equivalent, 18 had no significant change, and 15 had minor changes.
+ The identifier format changes from "3.1.1" (Rev 2) to "03.01.01" (Rev 3). Do not mix these formats in the same document.

## Preparing for the transition
<a name="preparing-for-the-transition"></a>

Organizations that implement Rev 2 well will be positioned for Rev 3, as the core security intent is consistent across revisions. To reduce future rework:
+ Structure your SSP sections modularly by control family so individual controls can be updated without rewriting the entire document.
+ Design automation (AWS Config rules, SCPs, conformance packs) with metadata tags that can accommodate Rev 3 control identifiers.
+ When building Rev 2 documentation, note the Rev 3 mapping where relevant.

Current engagements should focus on Rev 2 compliance while structuring documentation for Rev 3 adaptability.
