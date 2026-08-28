---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/step-1-design-you-third-party-module.html
---

# Step 1: Design your Third-Party Module
<a name="step-1-design-you-third-party-module"></a>

Beneath the surface, an MCS module is a CloudFormation stack defined by a CloudFormation template. When the module is registered with MCS, it is added to a product portfolio in Service Catalog.

MCS needs additional details about the module, such as the module type (for example, Network, Identity, Workstation Management, Storage, or Custom), revision, and dependencies on resources from other modules. This metadata is necessary for module discovery and registration.

To define a module, you need:
+ A CloudFormation template
+ Assets referenced by the template
+ Module metadata (as part of the CloudFormation template)
+ Module revision manifest file

Conceptually, registered module data is referenced as follows:

```
 Modular Cloud Studio on AWS
 \
 \ (Module)
 \-------------> Module Revision Manifest
|
|(1.0.0)
 +----------> AWS CloudFormation Template + Module Metadata
|\
|\---> CFN Resource Assets
|
|(2.0.0)
 +----------> AWS CloudFormation Template + Module Metadata
|\
|\---> CFN Resource Assets
|
|(2.1.0)
 +----------> AWS CloudFormation Template + Module Metadata
|\
|\---> CFN Resource Assets
|
|(3.0.0)
 +----------> AWS CloudFormation Template + Module Metadata
 Metadata
 \
 \---> CFN Resource Assets
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
