---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_VcfHostnames.html
---

# VcfHostnames
<a name="API_VcfHostnames"></a>

The DNS hostnames that Amazon EVS uses to install VMware vCenter Server, NSX, SDDC Manager, and Cloud Builder. Each hostname must be unique, and resolve to a domain name that you've registered in your DNS service of choice. Hostnames cannot be changed.

VMware VCF requires the deployment of two NSX Edge nodes, and three NSX Manager virtual machines.

**Note**
Not supported when `vcfVersion` is `SELF_DEPLOYED`.

## Contents
<a name="API_VcfHostnames_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** cloudBuilder **   <a name="evs-Type-VcfHostnames-cloudBuilder"></a>
The hostname for VMware Cloud Builder.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** nsx **   <a name="evs-Type-VcfHostnames-nsx"></a>
The VMware NSX Virtual IP (VIP) hostname.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** nsxEdge1 **   <a name="evs-Type-VcfHostnames-nsxEdge1"></a>
The hostname for the first NSX Edge node.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** nsxEdge2 **   <a name="evs-Type-VcfHostnames-nsxEdge2"></a>
The hostname for the second NSX Edge node.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** nsxManager1 **   <a name="evs-Type-VcfHostnames-nsxManager1"></a>
The hostname for the first VMware NSX Manager virtual machine (VM).
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** nsxManager2 **   <a name="evs-Type-VcfHostnames-nsxManager2"></a>
The hostname for the second VMware NSX Manager virtual machine (VM).
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** nsxManager3 **   <a name="evs-Type-VcfHostnames-nsxManager3"></a>
The hostname for the third VMware NSX Manager virtual machine (VM).
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** sddcManager **   <a name="evs-Type-VcfHostnames-sddcManager"></a>
The hostname for SDDC Manager.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

 ** vCenter **   <a name="evs-Type-VcfHostnames-vCenter"></a>
The VMware vCenter hostname.
Type: String
Pattern: `([a-zA-Z0-9\-]*)`
Required: Yes

## See Also
<a name="API_VcfHostnames_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/VcfHostnames)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/VcfHostnames)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/VcfHostnames)
