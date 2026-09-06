---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/classify-workload.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Classify workload
<a name="classify-workload"></a>

 The set of documents comprising the Cloud Security Guidance includes the [Health and Social Care Cloud Security – Good Practice Guide](https://digital.nhs.uk/data-and-information/looking-after-information/data-security-and-information-governance/nhs-and-social-care-data-off-shoring-and-the-use-of-public-cloud-services) (shortened to the *Good Practice Guide* in this paper), which describes five different classes of risk into which a given workload may fall. The primary determinants of the applicable class are:
+  The nature and volume of the data it processes
+  The duration for which they are stored
+  The data availability requirements (specifically as defined by NHS Digital’s Service Classification in *Appendix B* of the Good Practice Guide)

 The Good Practice Guide breaks down classifying a system into two stages:
+  Understanding the data
+  Assessing the risk

 Understanding the data entails gathering the characteristics listed above that determine how the workload is classified.

 To assess the risk, the NHS Guidance provides the [NHS Digital Data Risk Model](https://digital.nhs.uk/data-and-information/looking-after-information/data-security-and-information-governance/nhs-and-social-care-data-off-shoring-and-the-use-of-public-cloud-services), which computes the risk classification.

 There is an element of subjectivity and discretion in the inputs to the model, which potentially affects the workload’s classification. When providing the inputs, bear in mind that the higher the classification, the more controls required to manage the risk, and hence the greater the potential cost and complexity involved, which can increase operational risk rather than reduce it. It is important to achieve an appropriate balance between the risks to which the workload is subject and the costs of managing them effectively. If deciding between the deployment of a workload on-premises and cloud, it is equally important to compare the risks for both target environments.

 The risks in question sensibly cover not only the technical and organisational measures associated with managing risk, but a host of other considerations, such as public perception, lock-in risk, data repatriation, system complexity, data sovereignty, fair processing, documentation, and contracts. Though important, these are beyond the scope of this whitepaper. AWS recommends that customers who have concerns of this nature engage with their AWS account team to address these.
