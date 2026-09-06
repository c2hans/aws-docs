---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/stopping-intrusion-methods.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Stopping intrusion methods
<a name="stopping-intrusion-methods"></a>

 Understanding the stages or phases that attackers use to execute attacks can help security teams formulate ways to prevent successful attacks. Lockheed Martin’s intrusion kill chain framework describes a *courses of action matrix* (shown in the following table) that helps plan courses of action against each phase of any expected intrusion method. These actions include: detect, deny, disrupt, degrade, deceive, and destroy. (For definitions, see *Table 3* in [Modifications for the cloud](modifications-for-the-cloud.md).)

 **Table 1: Courses of action matrix**

|  Phase  |  Detect  |  Deny  |  Disrupt  |  Degrade  |  Deceive  |  Destroy  |
| --- | --- | --- | --- | --- | --- | --- |
|  Reconnaissance  |   |   |   |   |   |   |
|  Weaponization  |   |   |   |   |   |   |
|  Delivery  |   |   |   |   |   |   |
|  Exploitation  |   |   |   |   |   |   |
|  Installation  |   |   |   |   |   |   |
|  Command and Control  |   |   |   |   |   |   |
|  Actions on Objectives  |   |   |   |   |   |   |

 The concept of the matrix is for defenders to build capabilities that detect, deny, disrupt, degrade, deceive, and destroy attackers’ efforts in each phase of the intrusion. The goal is to stop the intrusion as early in the attack as possible because this reduces the recovery time, effort, cost, and damage associated with each attack. For example, detecting an attack in the *reconnaissance* phase is preferable to degrading the attack in the Command and Control (C2) phase.

**Topics**
+ [Modifications for the cloud](modifications-for-the-cloud.md)
+ [Sample mapping exercise](sample-mapping-exercise.md)
