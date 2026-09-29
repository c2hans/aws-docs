---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

Before you deploy the guidance:
+ Install [Git](https://git-scm.com/downloads).
+ Install Node.js 22 or later and npm.
+ Install Python 3.12.
+ Install Poetry 2 and the Poetry export plugin.
+ Install and configure the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ Create AWS CLI profiles for the Hub account, each Spoke account, and the Organizations management account.
+ Verify that the deployment identities can create AWS CDK and CloudFormation stacks and all resources defined by the stacks, including named IAM roles.
+ Record your organization ID, Organizations management account ID, Hub account ID, and each Spoke account ID.
+ Enable resource sharing with AWS Organizations in AWS RAM.

This guidance uses Amazon Cognito, which is not available in all AWS Regions. Choose a Region where Amazon Cognito and the other services used by the guidance are available. For current availability, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

## Activate AWS RAM for AWS Organizations accounts
<a name="activate-aws-ram-for-aws-organizations-accounts"></a>

Follow the instructions in [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the *AWS Resource Access Manager User Guide*.
