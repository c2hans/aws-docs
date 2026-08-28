---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/reference.html
---

# Reference
<a name="reference"></a>

This section includes information about an optional feature for collecting unique metrics for this solution, pointers to [related resources](#related-resources), and a [list of builders](#contributors) who contributed to this solution.

## Anonymized data collection
<a name="collection-of-operational-metrics"></a>

This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** − The AWS solution identifier
+  **Unique ID (UUID)** − Randomly generated, unique identifier for the Landing Zone Accelerator on AWS deployment
+  **Timestamp** − Data-collection timestamp

AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1. Download the [AWS CloudFormation template](https://s3.amazonaws.com/solutions-reference/landing-zone-accelerator-on-aws/latest/AWSAccelerator-InstallerStack.template) to your local hard drive.

1. Open the AWS CloudFormation template with a text editor.

1. Modify the AWS CloudFormation template mapping section from:

   ```
   AnonymizedData:
       SendAnonymizedData:
         Data: Yes
   ```

   to:

   ```
   AnonymizedData:
       SendAnonymizedData:
         Data: No
   ```

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1. Select **Create stack**.

1. On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1. Under **Upload a template file**, select **Choose file** and select the edited template from your local drive.

1. Choose **Next** and follow the steps in [Launch the stack](step-1.-launch-the-stack.md).

## Related resources
<a name="related-resources"></a>
+ Landing Zone Accelerator on AWS is a fully automated implementation of the architectural guidelines documented in the [AWS Security Reference Architecture (SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html).
+ Landing Zone Accelerator on AWS incorporates features and lessons learned from previous accelerator solutions such as the [Compliant Framework for Federal and DoD Workloads in GovCloud (US)](https://docs.aws.amazon.com/solutions/latest/compliant-framework-for-federal-and-dod-workloads-in-aws-govcloud-us/welcome.html) and the [AWS Secure Environment Accelerator](https://aws-samples.github.io/aws-secure-environment-accelerator/).

## Contributors
<a name="contributors"></a>
+ James Armitage
+ Mark Burr
+ Jimmy Clem
+ Brian Crissup
+ Partha Debnath
+ Randy Domingo
+ Dustin Hickey
+ Jason Johnson
+ Nagmesh Kumar
+ Bo Lechangeur
+ Ryan Cerrato
+ Eric Waxler
+ Melinda Mosholder
+ John Reynolds
+ Aasim Sayani
+ Jeremy Spell

 **United States (US) Federal and Department of Defense (DoD)**
+ Bhavish Khatri
+ Nagmesh Kumar

 **US aerospace**
+ Tim Sills

 **US state and local government Central IT**
+ Jason Hammett
+ Brian Stucker

 **Canadian Centre for Cyber Security (CCCS) Cloud Medium**
+ Brian Stucker
+ James Kierstead
+ Brian Mycroft
+ Donny Wilson
+ Tim Sills
+ Ryan Jaeger
+ Dave Liggat
+ JD Lynch
+ Lawrence Gohar
+ Sohaib Tahir
+ David Schmidt
+ Olivier Gaumond
+ Martin Guy Lapointe
+ Joel Desaulniers
+ Brent Fox
+ Dave Wood

 **Trusted Secure Enclaves Sensitive Edition (TSE-SE) for National Security, Defence, and National Law Enforcement reference architecture**
+ Brian Mycroft
+ Dave Liggat

 **United Kingdom (UK) National Cyber Security Centre (NCSC)**
+ Charlie Llewellyn
+ Muhammad Khas

 **Healthcare**
+ Donny Wison
+ Cate Hennard
+ Parthiban Dhayalan
+ Brian Stucker
+ Jason Hammett

 **Education**
+ Brian Stucker
+ Justin Haydt
+ Leo Zhadanovsky

 **Elections**
+ Lawrence Gohar

 **Finance (tax)**
+ Sohaib Tahir
+ David Schmidt
+ Brian Stucker

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
