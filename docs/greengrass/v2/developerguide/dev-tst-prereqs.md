---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/dev-tst-prereqs.html
---

# Prerequisites for running the AWS IoT Greengrass qualification suite
<a name="dev-tst-prereqs"></a>

This section describes the prerequisites for using AWS IoT Device Tester (IDT) for AWS IoT Greengrass.

## Download the latest version of AWS IoT Device Tester for AWS IoT Greengrass
<a name="install-dev-tst-gg"></a>

Download the [latest version](idt-programmatic-download.md) of IDT and extract the software into a location ({{<device-tester-extract-location>}}) on your file system where you have read/write permissions.

**Note**
<a name="unzip-package-to-local-drive"></a>IDT does not support being run by multiple users from a shared location, such as an NFS directory or a Windows network shared folder. We recommend that you extract the IDT package to a local drive and run the IDT binary on your local workstation.
Windows has a path length limitation of 260 characters. If you are using Windows, extract IDT to a root directory like `C:\ ` or `D:\` to keep your paths under the 260 character limit.

## Download the AWS IoT Greengrass software
<a name="config-gg"></a>

IDT for AWS IoT Greengrass V2 tests your device for compatibility with a specific version of AWS IoT Greengrass. Run the following command to download the AWS IoT Greengrass Core software to a file named `aws.greengrass.nucleus.zip`. Replace {{version}} with a [supported nucleus component version](dev-test-versions.md) for your IDT version.

------
#### [ Linux or Unix ]

```
curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-{{version}}.zip > aws.greengrass.nucleus.zip
```

------
#### [ Windows Command Prompt (CMD) ]

```
curl -s https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-{{version}}.zip > aws.greengrass.nucleus.zip
```

------
#### [ PowerShell ]

```
iwr -Uri https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-{{version}}.zip -OutFile aws.greengrass.nucleus.zip
```

------

Place the downloaded `aws.greengrass.nucleus.zip` file in the `{{<device-tester-extract-location>}}/products/` folder.

**Note**
Do not place multiple files in this directory for the same operating system and architecture.

## Create and configure an AWS account
<a name="config-aws-account-for-idt"></a>

Before you can use AWS IoT Device Tester for AWS IoT Greengrass V2, you must perform the following steps:

1. [Set up an AWS account.](#configure-idt-permissions) If you already have an AWS account, skip to step 2.

1. [Configure permissions for IDT.](#configure-idt-permissions)

These account permissions allow IDT to access AWS services and create AWS resources, such as AWS IoT things and AWS IoT Greengrass components, on your behalf.

<a name="idt-aws-credentials"></a>To create these resources, IDT for AWS IoT Greengrass V2 uses the AWS credentials configured in the `config.json` file to make API calls on your behalf. These resources are provisioned at various times during a test.

**Note**
Although most tests qualify for [AWS Free Tier](https://aws.amazon.com/free), you must provide a credit card when you sign up for an AWS account. For more information, see [ Why do I need a payment method if my account is covered by the Free Tier?](https://aws.amazon.com/premiumsupport/knowledge-center/free-tier-payment-method/).

### Step 2: Configure permissions for IDT
<a name="configure-idt-permissions"></a>

In this step, configure the permissions that IDT for AWS IoT Greengrass V2 uses to run tests and collect IDT usage data. You can use the [AWS Management Console](#configure-idt-permissions-console) or [AWS Command Line Interface (AWS CLI)](#configure-idt-permissions-cli) to create an IAM policy and a test user for IDT, and then attach policies to the user. If you already created a test user for IDT, skip to [Configure your device to run IDT tests](device-config-setup.md).

#### To configure permissions for IDT (console)
<a name="configure-idt-permissions-console"></a>

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam).

1. Create a customer managed policy that grants permissions to create roles with specific permissions.

   1. In the navigation pane, choose **Policies**, and then choose **Create policy**.

   1. If you are not using PreInstalled, on the **JSON** tab, replace the placeholder content with the following policy. If you are using PreInstalled, proceed to the following step.

      ```
      <a name="customer-managed-policy-cli"></a>{
          "Version":"2012-10-17",
          "Statement":[
          {
            "Sid":"passRoleForResources",
            "Effect":"Allow",
            "Action":"iam:PassRole",
            "Resource":"arn:aws:iam::*:role/idt-*",
            "Condition":{
              "StringEquals":{
                "iam:PassedToService":[
                  "iot.amazonaws.com",
                  "lambda.amazonaws.com",
                  "greengrass.amazonaws.com"
                ]
              }
            }
          },
          {
            "Sid":"lambdaResources",
            "Effect":"Allow",
            "Action":[
              "lambda:CreateFunction",
              "lambda:PublishVersion",
              "lambda:DeleteFunction",
              "lambda:GetFunction"
            ],
            "Resource":[
              "arn:aws:lambda:*:*:function:idt-*"
            ]
          },
          {
            "Sid":"iotResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateThing",
              "iot:DeleteThing",
              "iot:DescribeThing",
              "iot:CreateThingGroup",
              "iot:DeleteThingGroup",
              "iot:DescribeThingGroup",
              "iot:AddThingToThingGroup",
              "iot:RemoveThingFromThingGroup",
              "iot:AttachThingPrincipal",
              "iot:DetachThingPrincipal",
              "iot:UpdateCertificate",
              "iot:DeleteCertificate",
              "iot:CreatePolicy",
              "iot:AttachPolicy",
              "iot:DetachPolicy",
              "iot:DeletePolicy",
              "iot:GetPolicy",
              "iot:Publish",
              "iot:TagResource",
              "iot:ListThingPrincipals",
              "iot:ListAttachedPolicies",
              "iot:ListTargetsForPolicy",
              "iot:ListThingGroupsForThing",
              "iot:ListThingsInThingGroup",
              "iot:CreateJob",
              "iot:DescribeJob",
              "iot:DescribeJobExecution",
              "iot:CancelJob"
            ],
            "Resource":[
              "arn:aws:iot:*:*:thing/idt-*",
              "arn:aws:iot:*:*:thinggroup/idt-*",
              "arn:aws:iot:*:*:policy/idt-*",
              "arn:aws:iot:*:*:cert/*",
              "arn:aws:iot:*:*:topic/idt-*",
              "arn:aws:iot:*:*:job/*"
            ]
          },
          {
            "Sid":"s3Resources",
            "Effect":"Allow",
            "Action":[
              "s3:GetObject",
              "s3:PutObject",
              "s3:DeleteObjectVersion",
              "s3:DeleteObject",
              "s3:CreateBucket",
              "s3:ListBucket",
              "s3:ListBucketVersions",
              "s3:DeleteBucket",
              "s3:PutObjectTagging",
              "s3:PutBucketTagging"
            ],
            "Resource":"arn:aws:s3::*:idt-*"
          },
          {
            "Sid":"roleAliasResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateRoleAlias",
              "iot:DescribeRoleAlias",
              "iot:DeleteRoleAlias",
              "iot:TagResource",
              "iam:GetRole"
            ],
            "Resource":[
              "arn:aws:iot:*:*:rolealias/idt-*",
              "arn:aws:iam::*:role/idt-*"
            ]
          },
          {
            "Sid":"idtExecuteAndCollectMetrics",
            "Effect":"Allow",
            "Action":[
              "iot-device-tester:SendMetrics",
              "iot-device-tester:SupportedVersion",
              "iot-device-tester:LatestIdt",
              "iot-device-tester:CheckVersion",
              "iot-device-tester:DownloadTestSuite"
            ],
            "Resource":"*"
          },
          {
            "Sid":"genericResources",
            "Effect":"Allow",
            "Action":[
              "greengrass:*",
              "iot:GetThingShadow",
              "iot:UpdateThingShadow",
              "iot:ListThings",
              "iot:DescribeEndpoint",
              "iot:CreateKeysAndCertificate"
            ],
            "Resource":"*"
          },
          {
            "Sid":"iamResourcesUpdate",
            "Effect":"Allow",
            "Action":[
              "iam:CreateRole",
              "iam:DeleteRole",
              "iam:CreatePolicy",
              "iam:DeletePolicy",
              "iam:AttachRolePolicy",
              "iam:DetachRolePolicy",
              "iam:TagRole",
              "iam:TagPolicy",
              "iam:GetPolicy",
              "iam:ListAttachedRolePolicies",
              "iam:ListEntitiesForPolicy"
            ],
            "Resource":[
              "arn:aws:iam::*:role/idt-*",
              "arn:aws:iam::*:policy/idt-*"
            ]
          }
        ]
      }
      ```

   1. If you are using PreInstalled, on the **JSON** tab, replace the placeholder content with the following policy. Make sure you:
      + Replace {{thingName}} and {{thingGroup}} in the `iotResources` statement with the thing name and thing group that were created during the Greengrass installation on your device under test (DUT) to add permissions.
      + Replace the {{passRole}} and {{roleAlias}} in the `roleAliasResources` statement and the `passRoleForResources` statement with the roles that were created during the Greengrass installation on your DUT.

      ```
      <a name="customer-managed-policy-cli"></a>{
          "Version":"2012-10-17",
          "Statement":[
          {
            "Sid":"passRoleForResources",
            "Effect":"Allow",
            "Action":"iam:PassRole",
            "Resource":"arn:aws:iam::*:role/{{passRole}}",
            "Condition":{
              "StringEquals":{
                "iam:PassedToService":[
                  "iot.amazonaws.com",
                  "lambda.amazonaws.com",
                  "greengrass.amazonaws.com"
                ]
              }
            }
          },
          {
            "Sid":"lambdaResources",
            "Effect":"Allow",
            "Action":[
              "lambda:CreateFunction",
              "lambda:PublishVersion",
              "lambda:DeleteFunction",
              "lambda:GetFunction"
            ],
            "Resource":[
              "arn:aws:lambda:*:*:function:idt-*"
            ]
          },
          {
            "Sid":"iotResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateThing",
              "iot:DeleteThing",
              "iot:DescribeThing",
              "iot:CreateThingGroup",
              "iot:DeleteThingGroup",
              "iot:DescribeThingGroup",
              "iot:AddThingToThingGroup",
              "iot:RemoveThingFromThingGroup",
              "iot:AttachThingPrincipal",
              "iot:DetachThingPrincipal",
              "iot:UpdateCertificate",
              "iot:DeleteCertificate",
              "iot:CreatePolicy",
              "iot:AttachPolicy",
              "iot:DetachPolicy",
              "iot:DeletePolicy",
              "iot:GetPolicy",
              "iot:Publish",
              "iot:TagResource",
              "iot:ListThingPrincipals",
              "iot:ListAttachedPolicies",
              "iot:ListTargetsForPolicy",
              "iot:ListThingGroupsForThing",
              "iot:ListThingsInThingGroup",
              "iot:CreateJob",
              "iot:DescribeJob",
              "iot:DescribeJobExecution",
              "iot:CancelJob"
            ],
            "Resource":[
              "arn:aws:iot:*:*:thing/{{thingName}}",
              "arn:aws:iot:*:*:thinggroup/{{thingGroup}}",
              "arn:aws:iot:*:*:policy/idt-*",
              "arn:aws:iot:*:*:cert/*",
              "arn:aws:iot:*:*:topic/idt-*",
              "arn:aws:iot:*:*:job/*"
            ]
          },
          {
            "Sid":"s3Resources",
            "Effect":"Allow",
            "Action":[
              "s3:GetObject",
              "s3:PutObject",
              "s3:DeleteObjectVersion",
              "s3:DeleteObject",
              "s3:CreateBucket",
              "s3:ListBucket",
              "s3:ListBucketVersions",
              "s3:DeleteBucket",
              "s3:PutObjectTagging",
              "s3:PutBucketTagging"
            ],
            "Resource":"arn:aws:s3::*:idt-*"
          },
          {
            "Sid":"roleAliasResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateRoleAlias",
              "iot:DescribeRoleAlias",
              "iot:DeleteRoleAlias",
              "iot:TagResource",
              "iam:GetRole"
            ],
            "Resource":[
              "arn:aws:iot:*:*:rolealias/{{roleAlias}}",
              "arn:aws:iam::*:role/idt-*"
            ]
          },
          {
            "Sid":"idtExecuteAndCollectMetrics",
            "Effect":"Allow",
            "Action":[
              "iot-device-tester:SendMetrics",
              "iot-device-tester:SupportedVersion",
              "iot-device-tester:LatestIdt",
              "iot-device-tester:CheckVersion",
              "iot-device-tester:DownloadTestSuite"
            ],
            "Resource":"*"
          },
          {
            "Sid":"genericResources",
            "Effect":"Allow",
            "Action":[
              "greengrass:*",
              "iot:GetThingShadow",
              "iot:UpdateThingShadow",
              "iot:ListThings",
              "iot:DescribeEndpoint",
              "iot:CreateKeysAndCertificate"
            ],
            "Resource":"*"
          },
          {
            "Sid":"iamResourcesUpdate",
            "Effect":"Allow",
            "Action":[
              "iam:CreateRole",
              "iam:DeleteRole",
              "iam:CreatePolicy",
              "iam:DeletePolicy",
              "iam:AttachRolePolicy",
              "iam:DetachRolePolicy",
              "iam:TagRole",
              "iam:TagPolicy",
              "iam:GetPolicy",
              "iam:ListAttachedRolePolicies",
              "iam:ListEntitiesForPolicy"
            ],
            "Resource":[
              "arn:aws:iam::*:role/idt-*",
              "arn:aws:iam::*:policy/idt-*"
            ]
          }
        ]
      }
      ```
**Note**
If you want to use a [custom IAM role as the token exchange role](set-config.md#custom-token-exchange-role-idt) for your device under test, make sure you update the `roleAliasResources` statement and the `passRoleForResources` statement in your policy to allow your custom IAM role resource.

   1. Choose **Review policy**.

   1. For **Name**, enter **IDTGreengrassIAMPermissions**. Under **Summary**, review the permissions granted by your policy.

   1. Choose **Create policy**.

1. Create an IAM user and attach the permissions required by IDT for AWS IoT Greengrass.

   1. Create an IAM user. Follow steps 1 through 5 in [Creating IAM users (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) in the *IAM User Guide*.

   1. Attach the permissions to your IAM user:

      1. On the **Set permissions ** page, choose **Attach existing policies to user directly**.

      1. Search for the **IDTGreengrassIAMPermissions** policy that you created in the previous step. Select the check box.

   1. Choose **Next: Tags**.

   1. Choose **Next: Review** to view a summary of your choices.

   1. Choose **Create user**.

   1. To view the user's access keys (access key IDs and secret access keys), choose **Show** next to the password and access key. To save the access keys, choose **Download.csv** and save the file to a secure location. You use this information later to configure your AWS credentials file.

1. <a name="aws-account-config-next-steps"></a>Next step: Configure your [physical device](device-config-setup.md).

#### To configure permissions for IDT (AWS CLI)
<a name="configure-idt-permissions-cli"></a>

1. On your computer, install and configure the AWS CLI if it's not already installed. Follow the steps in [ Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the *AWS Command Line Interface User Guide*.
**Note**
The AWS CLI is an open source tool that you can use to interact with AWS services from your command-line shell.

1. Create a customer managed policy that grants permissions to manage IDT and AWS IoT Greengrass roles.

   1. If you are not using PreInstalled, open a text editor and save the following policy contents in a JSON file. If you are using PreInstalled, proceed to the following step.

      ```
      <a name="customer-managed-policy-cli"></a>{
          "Version":"2012-10-17",
          "Statement":[
          {
            "Sid":"passRoleForResources",
            "Effect":"Allow",
            "Action":"iam:PassRole",
            "Resource":"arn:aws:iam::*:role/idt-*",
            "Condition":{
              "StringEquals":{
                "iam:PassedToService":[
                  "iot.amazonaws.com",
                  "lambda.amazonaws.com",
                  "greengrass.amazonaws.com"
                ]
              }
            }
          },
          {
            "Sid":"lambdaResources",
            "Effect":"Allow",
            "Action":[
              "lambda:CreateFunction",
              "lambda:PublishVersion",
              "lambda:DeleteFunction",
              "lambda:GetFunction"
            ],
            "Resource":[
              "arn:aws:lambda:*:*:function:idt-*"
            ]
          },
          {
            "Sid":"iotResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateThing",
              "iot:DeleteThing",
              "iot:DescribeThing",
              "iot:CreateThingGroup",
              "iot:DeleteThingGroup",
              "iot:DescribeThingGroup",
              "iot:AddThingToThingGroup",
              "iot:RemoveThingFromThingGroup",
              "iot:AttachThingPrincipal",
              "iot:DetachThingPrincipal",
              "iot:UpdateCertificate",
              "iot:DeleteCertificate",
              "iot:CreatePolicy",
              "iot:AttachPolicy",
              "iot:DetachPolicy",
              "iot:DeletePolicy",
              "iot:GetPolicy",
              "iot:Publish",
              "iot:TagResource",
              "iot:ListThingPrincipals",
              "iot:ListAttachedPolicies",
              "iot:ListTargetsForPolicy",
              "iot:ListThingGroupsForThing",
              "iot:ListThingsInThingGroup",
              "iot:CreateJob",
              "iot:DescribeJob",
              "iot:DescribeJobExecution",
              "iot:CancelJob"
            ],
            "Resource":[
              "arn:aws:iot:*:*:thing/idt-*",
              "arn:aws:iot:*:*:thinggroup/idt-*",
              "arn:aws:iot:*:*:policy/idt-*",
              "arn:aws:iot:*:*:cert/*",
              "arn:aws:iot:*:*:topic/idt-*",
              "arn:aws:iot:*:*:job/*"
            ]
          },
          {
            "Sid":"s3Resources",
            "Effect":"Allow",
            "Action":[
              "s3:GetObject",
              "s3:PutObject",
              "s3:DeleteObjectVersion",
              "s3:DeleteObject",
              "s3:CreateBucket",
              "s3:ListBucket",
              "s3:ListBucketVersions",
              "s3:DeleteBucket",
              "s3:PutObjectTagging",
              "s3:PutBucketTagging"
            ],
            "Resource":"arn:aws:s3::*:idt-*"
          },
          {
            "Sid":"roleAliasResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateRoleAlias",
              "iot:DescribeRoleAlias",
              "iot:DeleteRoleAlias",
              "iot:TagResource",
              "iam:GetRole"
            ],
            "Resource":[
              "arn:aws:iot:*:*:rolealias/idt-*",
              "arn:aws:iam::*:role/idt-*"
            ]
          },
          {
            "Sid":"idtExecuteAndCollectMetrics",
            "Effect":"Allow",
            "Action":[
              "iot-device-tester:SendMetrics",
              "iot-device-tester:SupportedVersion",
              "iot-device-tester:LatestIdt",
              "iot-device-tester:CheckVersion",
              "iot-device-tester:DownloadTestSuite"
            ],
            "Resource":"*"
          },
          {
            "Sid":"genericResources",
            "Effect":"Allow",
            "Action":[
              "greengrass:*",
              "iot:GetThingShadow",
              "iot:UpdateThingShadow",
              "iot:ListThings",
              "iot:DescribeEndpoint",
              "iot:CreateKeysAndCertificate"
            ],
            "Resource":"*"
          },
          {
            "Sid":"iamResourcesUpdate",
            "Effect":"Allow",
            "Action":[
              "iam:CreateRole",
              "iam:DeleteRole",
              "iam:CreatePolicy",
              "iam:DeletePolicy",
              "iam:AttachRolePolicy",
              "iam:DetachRolePolicy",
              "iam:TagRole",
              "iam:TagPolicy",
              "iam:GetPolicy",
              "iam:ListAttachedRolePolicies",
              "iam:ListEntitiesForPolicy"
            ],
            "Resource":[
              "arn:aws:iam::*:role/idt-*",
              "arn:aws:iam::*:policy/idt-*"
            ]
          }
        ]
      }
      ```

   1. If you are using PreInstalled, open a text editor and save the following policy contents in a JSON file. Make sure you:
      + Replace {{thingName}} and {{thingGroup}} in the `iotResources` statement that were created during the Greengrass installation on your device under test (DUT) to add permissions.
      + Replace the {{passRole}} and {{roleAlias}} in the `roleAliasResources` statement and the `passRoleForResources` statement with the roles that were created during the Greengrass installation on your DUT.

      ```
      <a name="customer-managed-policy-cli"></a>{
          "Version":"2012-10-17",
          "Statement":[
          {
            "Sid":"passRoleForResources",
            "Effect":"Allow",
            "Action":"iam:PassRole",
            "Resource":"arn:aws:iam::*:role/{{passRole}}",
            "Condition":{
              "StringEquals":{
                "iam:PassedToService":[
                  "iot.amazonaws.com",
                  "lambda.amazonaws.com",
                  "greengrass.amazonaws.com"
                ]
              }
            }
          },
          {
            "Sid":"lambdaResources",
            "Effect":"Allow",
            "Action":[
              "lambda:CreateFunction",
              "lambda:PublishVersion",
              "lambda:DeleteFunction",
              "lambda:GetFunction"
            ],
            "Resource":[
              "arn:aws:lambda:*:*:function:idt-*"
            ]
          },
          {
            "Sid":"iotResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateThing",
              "iot:DeleteThing",
              "iot:DescribeThing",
              "iot:CreateThingGroup",
              "iot:DeleteThingGroup",
              "iot:DescribeThingGroup",
              "iot:AddThingToThingGroup",
              "iot:RemoveThingFromThingGroup",
              "iot:AttachThingPrincipal",
              "iot:DetachThingPrincipal",
              "iot:UpdateCertificate",
              "iot:DeleteCertificate",
              "iot:CreatePolicy",
              "iot:AttachPolicy",
              "iot:DetachPolicy",
              "iot:DeletePolicy",
              "iot:GetPolicy",
              "iot:Publish",
              "iot:TagResource",
              "iot:ListThingPrincipals",
              "iot:ListAttachedPolicies",
              "iot:ListTargetsForPolicy",
              "iot:ListThingGroupsForThing",
              "iot:ListThingsInThingGroup",
              "iot:CreateJob",
              "iot:DescribeJob",
              "iot:DescribeJobExecution",
              "iot:CancelJob"
            ],
            "Resource":[
              "arn:aws:iot:*:*:thing/{{thingName}}",
              "arn:aws:iot:*:*:thinggroup/{{thingGroup}}",
              "arn:aws:iot:*:*:policy/idt-*",
              "arn:aws:iot:*:*:cert/*",
              "arn:aws:iot:*:*:topic/idt-*",
              "arn:aws:iot:*:*:job/*"
            ]
          },
          {
            "Sid":"s3Resources",
            "Effect":"Allow",
            "Action":[
              "s3:GetObject",
              "s3:PutObject",
              "s3:DeleteObjectVersion",
              "s3:DeleteObject",
              "s3:CreateBucket",
              "s3:ListBucket",
              "s3:ListBucketVersions",
              "s3:DeleteBucket",
              "s3:PutObjectTagging",
              "s3:PutBucketTagging"
            ],
            "Resource":"arn:aws:s3::*:idt-*"
          },
          {
            "Sid":"roleAliasResources",
            "Effect":"Allow",
            "Action":[
              "iot:CreateRoleAlias",
              "iot:DescribeRoleAlias",
              "iot:DeleteRoleAlias",
              "iot:TagResource",
              "iam:GetRole"
            ],
            "Resource":[
              "arn:aws:iot:*:*:rolealias/{{roleAlias}}",
              "arn:aws:iam::*:role/idt-*"
            ]
          },
          {
            "Sid":"idtExecuteAndCollectMetrics",
            "Effect":"Allow",
            "Action":[
              "iot-device-tester:SendMetrics",
              "iot-device-tester:SupportedVersion",
              "iot-device-tester:LatestIdt",
              "iot-device-tester:CheckVersion",
              "iot-device-tester:DownloadTestSuite"
            ],
            "Resource":"*"
          },
          {
            "Sid":"genericResources",
            "Effect":"Allow",
            "Action":[
              "greengrass:*",
              "iot:GetThingShadow",
              "iot:UpdateThingShadow",
              "iot:ListThings",
              "iot:DescribeEndpoint",
              "iot:CreateKeysAndCertificate"
            ],
            "Resource":"*"
          },
          {
            "Sid":"iamResourcesUpdate",
            "Effect":"Allow",
            "Action":[
              "iam:CreateRole",
              "iam:DeleteRole",
              "iam:CreatePolicy",
              "iam:DeletePolicy",
              "iam:AttachRolePolicy",
              "iam:DetachRolePolicy",
              "iam:TagRole",
              "iam:TagPolicy",
              "iam:GetPolicy",
              "iam:ListAttachedRolePolicies",
              "iam:ListEntitiesForPolicy"
            ],
            "Resource":[
              "arn:aws:iam::*:role/idt-*",
              "arn:aws:iam::*:policy/idt-*"
            ]
          }
        ]
      }
      ```
**Note**
If you want to use a [custom IAM role as the token exchange role](set-config.md#custom-token-exchange-role-idt) for your device under test, make sure you update the `roleAliasResources` statement and the `passRoleForResources` statement in your policy to allow your custom IAM role resource.

   1. Run the following command to create a customer managed policy named `IDTGreengrassIAMPermissions`. Replace `{{policy.json}}` with the full path to the JSON file that you created in the previous step.

      ```
      aws iam create-policy --policy-name IDTGreengrassIAMPermissions --policy-document file://{{policy.json}}
      ```

1. Create an IAM user and attach the permissions required by IDT for AWS IoT Greengrass.

   1. Create an IAM user. In this example setup, the user is named `IDTGreengrassUser`.

      ```
      aws iam create-user --user-name IDTGreengrassUser
      ```

   1. Attach the `IDTGreengrassIAMPermissions` policy you created in step 2 to your IAM user. Replace {{<account-id>}} in the command with the ID of your AWS account.

      ```
      aws iam attach-user-policy --user-name IDTGreengrassUser --policy-arn arn:aws:iam::{{<account-id>}}:policy/IDTGreengrassIAMPermissions
      ```

1. Create a secret access key for the user.

   ```
   aws iam create-access-key --user-name IDTGreengrassUser
   ```

   Store the output in a secure location. You use this information later to configure your AWS credentials file.

1. <a name="aws-account-config-next-steps"></a>Next step: Configure your [physical device](device-config-setup.md).

### AWS IoT Device Tester permissions
<a name="gg-idt-managed-policy"></a>

The following policies describe AWS IoT Device Tester permissions.

AWS IoT Device Tester requires these permissions for version checking and auto-update features.
+ `iot-device-tester:SupportedVersion`

  Grants AWS IoT Device Tester permission to fetch the list of supported products, test suites and IDT versions.
+ `iot-device-tester:LatestIdt`

  Grants AWS IoT Device Tester permission to fetch the latest IDT version available for download.
+ `iot-device-tester:CheckVersion`

  Grants AWS IoT Device Tester permission to check version compatibility for IDT, test suites and products.
+ `iot-device-tester:DownloadTestSuite`

  Grants AWS IoT Device Tester permission to download test suites updates.

AWS IoT Device Tester also uses the following permission for optional metrics reporting:
+ `iot-device-tester:SendMetrics`

  Grants permission to AWS to collect metrics about AWS IoT Device Tester internal usage. If this permission is omitted, these metrics will not be collected.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
