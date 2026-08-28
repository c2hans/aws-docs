---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-vcfhostnames.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment VcfHostnames
<a name="aws-properties-evs-environment-vcfhostnames"></a>

The DNS hostnames that Amazon EVS uses to install VMware vCenter Server, NSX, SDDC Manager, and Cloud Builder. Each hostname must be unique, and resolve to a domain name that you've registered in your DNS service of choice. Hostnames cannot be changed.

VMware VCF requires the deployment of two NSX Edge nodes, and three NSX Manager virtual machines.

**Note**
Not supported when `vcfVersion` is `SELF_DEPLOYED`.

## Syntax
<a name="aws-properties-evs-environment-vcfhostnames-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-vcfhostnames-syntax.json"></a>

```
{
  "[CloudBuilder](#cfn-evs-environment-vcfhostnames-cloudbuilder)" : {{String}},
  "[Nsx](#cfn-evs-environment-vcfhostnames-nsx)" : {{String}},
  "[NsxEdge1](#cfn-evs-environment-vcfhostnames-nsxedge1)" : {{String}},
  "[NsxEdge2](#cfn-evs-environment-vcfhostnames-nsxedge2)" : {{String}},
  "[NsxManager1](#cfn-evs-environment-vcfhostnames-nsxmanager1)" : {{String}},
  "[NsxManager2](#cfn-evs-environment-vcfhostnames-nsxmanager2)" : {{String}},
  "[NsxManager3](#cfn-evs-environment-vcfhostnames-nsxmanager3)" : {{String}},
  "[SddcManager](#cfn-evs-environment-vcfhostnames-sddcmanager)" : {{String}},
  "[VCenter](#cfn-evs-environment-vcfhostnames-vcenter)" : {{String}}
}
```

### YAML
<a name="aws-properties-evs-environment-vcfhostnames-syntax.yaml"></a>

```
  [CloudBuilder](#cfn-evs-environment-vcfhostnames-cloudbuilder): {{String}}
  [Nsx](#cfn-evs-environment-vcfhostnames-nsx): {{String}}
  [NsxEdge1](#cfn-evs-environment-vcfhostnames-nsxedge1): {{String}}
  [NsxEdge2](#cfn-evs-environment-vcfhostnames-nsxedge2): {{String}}
  [NsxManager1](#cfn-evs-environment-vcfhostnames-nsxmanager1): {{String}}
  [NsxManager2](#cfn-evs-environment-vcfhostnames-nsxmanager2): {{String}}
  [NsxManager3](#cfn-evs-environment-vcfhostnames-nsxmanager3): {{String}}
  [SddcManager](#cfn-evs-environment-vcfhostnames-sddcmanager): {{String}}
  [VCenter](#cfn-evs-environment-vcfhostnames-vcenter): {{String}}
```

## Properties
<a name="aws-properties-evs-environment-vcfhostnames-properties"></a>

`CloudBuilder`  <a name="cfn-evs-environment-vcfhostnames-cloudbuilder"></a>
The hostname for VMware Cloud Builder.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`Nsx`  <a name="cfn-evs-environment-vcfhostnames-nsx"></a>
The VMware NSX Virtual IP (VIP) hostname.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`NsxEdge1`  <a name="cfn-evs-environment-vcfhostnames-nsxedge1"></a>
The hostname for the first NSX Edge node.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`NsxEdge2`  <a name="cfn-evs-environment-vcfhostnames-nsxedge2"></a>
The hostname for the second NSX Edge node.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`NsxManager1`  <a name="cfn-evs-environment-vcfhostnames-nsxmanager1"></a>
The hostname for the first VMware NSX Manager virtual machine (VM).
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`NsxManager2`  <a name="cfn-evs-environment-vcfhostnames-nsxmanager2"></a>
The hostname for the second VMware NSX Manager virtual machine (VM).
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`NsxManager3`  <a name="cfn-evs-environment-vcfhostnames-nsxmanager3"></a>
The hostname for the third VMware NSX Manager virtual machine (VM).
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`SddcManager`  <a name="cfn-evs-environment-vcfhostnames-sddcmanager"></a>
The hostname for SDDC Manager.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

`VCenter`  <a name="cfn-evs-environment-vcfhostnames-vcenter"></a>
The VMware vCenter hostname.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9\-]*)$`
*Update requires*: Updates are not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
