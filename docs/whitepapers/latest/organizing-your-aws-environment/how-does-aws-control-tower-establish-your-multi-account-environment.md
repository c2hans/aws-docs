---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/how-does-aws-control-tower-establish-your-multi-account-environment.html
---

# How does AWS Control Tower establish your multi-account environment?
<a name="how-does-aws-control-tower-establish-your-multi-account-environment"></a>

 AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment, following prescriptive best practices. AWS Control Tower *orchestrates* the capabilities of several other AWS services, including AWS Organizations, Service Catalog, and AWS IAM Identity Center. This section describes at a high level how AWS Control Tower establish a multi-account environment and landing zone. Your landing zone is a well-architected multi-account environment for all of your AWS resources. You can use this environment to enforce compliance regulations on all of your AWS accounts.

**Topics**
+ [Establish your multi-account environment with AWS Control Tower](#establish-your-multi-account-environment-with-aws-control-tower)
+ [Next steps for setting up your multi-account environment](#next-steps-for-setting-up-your-multi-account-environment)

## Establish your multi-account environment with AWS Control Tower
<a name="establish-your-multi-account-environment-with-aws-control-tower"></a>

 When you set up your multi-account environment using AWS Control Tower, it creates two OUs.
+ Security OU—Within this OU, AWS Control Tower creates two accounts:
  + Log Archive
  + Audit (This account corresponds to the Security Tooling account discussed previously in the guidance.)
+ Sandbox OU—This OU is the default destination for accounts created within AWS Control Tower. It contains accounts in which your builders can explore and experiment with AWS services, and other tools and services, subject to your team's acceptable use policies.

![Diagram showing the OUs and accounts created by AWS Control Tower](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/ous-accounts-by-control-tower.png)

 **AWS Control Tower allows you to create, register, and manage additional OUs to expand the initial environment to implement the guidance.**

 The following diagram shows the OUs initially deployed by AWS Control Tower. You can expand your AWS environment to implement any of the recommended OUs included in the diagram, to meet your requirements.

![Diagram showing OUs initially deployed by AWS Control Tower](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/initial-ous-by-control-tower.png)

## Next steps for setting up your multi-account environment
<a name="next-steps-for-setting-up-your-multi-account-environment"></a>

 To get started with AWS Control Tower, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html). We recommend that you review the prerequisites and next steps required to establish your multi-account environment on AWS.

For complete guidance on establishing your multi-account environment, review the guidance included in this whitepaper.
