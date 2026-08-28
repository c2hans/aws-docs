---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/governance-and-control.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Governance and control
<a name="governance-and-control"></a>

## Guardrails
<a name="guardrails"></a>

Large enterprises with strict security and compliance requirements need to set up guardrails for operating the ML environments. IAM policies can be used for enforcing guardrails, such as requiring proper resource tagging or limiting type of resources used, for different users and roles. For enterprise scale guardrail management, consider [AWS Organizations](https://aws.amazon.com/organizations/). Its Service Control Policies (SCP) feature can help with enterprise guardrail management, by attaching a SCP to an AWS Organizations entity (root, organizational unit (OU), or account). You still need to attach [identity-based or resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) to IAM users or roles, or to the resources in your organization's accounts to actually grant permissions. When an IAM user or role belongs to an account that is a member of an organization, the SCPs can limit the user's or role's [effective permissions](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html#scp-effects-on-permissions).

![A diagram that shows managing guardrails with AWS Organizations and Service Control Policies.](http://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/images/build-ml-17.png)

*Managing guardrails with AWS Organizations and Service Control Policies*

### Enforcing encryption
<a name="enforcing-encryption"></a>
+ **Enforcing notebook encryption** — SageMaker AI Notebook Instance EBS volume encryption can be enforced using the `sagemaker:VolumeKmsKey` condition key.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerNoteBookEnforceEncryption",
        "Effect": "Deny",
        "Action": [
          "sagemaker:CreateNotebookInstance",
          "sagemaker:UpdateNotebookInstance"
        ],
        "Resource": "*",
        "Condition": {
          "Null": {
            "sagemaker:VolumeKmsKey": "true"
          }
        }
      }
    ]
  }
  ```

------
+ **Enforcing Studio Notebook EFS encryption** — The EFS storage encryption can be enforced using the `sagemaker:VolumeKmsKey` condition key.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerStudioEnforceEncryption",
        "Effect": "Deny",
        "Action": [
          "sagemaker:CreateDomain"
        ],
        "Resource": "*",
        "Condition": {
          "Null": {
            "sagemaker:VolumeKmsKey": "true"
          }
        }
      }
    ]
  }
  ```

------
+ **Enforcing job encryption **— Similarly, encryption for the SageMaker AI training job, processing job, transform job, and hyperparameter tuning job can be enforced using the `sagemaker:VolumeKmsKey` condition key.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerJobEnforceEncryption",
        "Effect": "Deny",
        "Action": [
          "sagemaker:CreateHyperParameterTuningJob",
          "sagemaker:CreateProcessingJob",
          "sagemaker:CreateTrainingJob",
          "sagemaker:CreateTransformJob"
        ],
        "Resource": "*",
        "Condition": {
          "Null": {
            "sagemaker:VolumeKmsKey": "true"
          }
        }
      }
    ]
  }
  ```

------
+ **Enforcing inter-container traffic encryption** — For extremely sensitive distributed model training job and tuning job, the `sagemaker:InterContainerTrafficEncryption` condition key can be used to encrypt inter-container traffic.
**Note**
 The training speed will be negatively impacted when this is enabled.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerEnforceInterContainerTrafficEncryption",
        "Effect": "Deny",
        "Action": [
          "sagemaker:CreateHyperParameterTuningJob",
          "sagemaker:CreateTrainingJob"
        ],
        "Resource": "*",
        "Condition": {
          "Bool": {
            "sagemaker:InterContainerTrafficEncryption": "false"
          }
        }
      }
    ]
  }
  ```

------

### Controlling data egress
<a name="controlling-data-egress"></a>
+ **Enforcing deployment in VPC** — To route traffic from SageMaker to access resources in a VPC, `sagemaker:VpcSubnets` and `sagemaker:VpcSecurityGroupIds` can be used to configure VPC and security group to manage the traffic.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerEnforceVPCDeployment",
        "Effect": "Deny",
        "Action": [
          "sagemaker:CreateHyperParameterTuningJob",
          "sagemaker:CreateModel",
          "sagemaker:CreateNotebookInstance",
          "sagemaker:CreateProcessingJob",
          "sagemaker:CreateTrainingJob"
        ],
        "Resource": "*",
        "Condition": {
          "Null": {
            "sagemaker:VpcSubnets": "true",
            "sagemaker:VpcSecurityGroupIds": "true"
          }
        }
      }
    ]
  }
  ```

------
+ **Enforcing Network Isolation** — Networking traffic can be blocked for the algorithm container using the `sagemaker:NetworkIsolation` condition key.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "NetworkIsolation",
      "Effect": "Deny",
      "Action": [
        "sagemaker:CreateHyperParameterTuningJob",
        "sagemaker:CreateTrainingJob"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "sagemaker:NetworkIsolation": "false"
          }
        }
      }
    ]
  }
  ```

------
+ Restricting access to SageMaker AI API and runtime by IP address — You can restrict the IP address ranges for invoking different SageMaker AI APIs by using the `aws:SourceIp` condition key.
+ Restricting Studio and notebook pre-signed URLs to IPs — Launching SageMaker AI Studio or SageMaker AI Notebook instance can be restricted by the `aws:SourceIp`.

### Disabling internet access
<a name="disabling-internet-access"></a>
+ **Disabling SageMaker AI Notebook internet access** — If you want to disable internet access when the notebook is created, you can use `sagemaker:DirectInternetAccess` to achieve this.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerPreventDirectInternet",
        "Effect": "Deny",
        "Action": "sagemaker:CreateNotebookInstance",
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "sagemaker:DirectInternetAccess": [
              "Enabled"
            ]
          }
        }
      }
    ]
  }
  ```

------
+ **Disabling Studio Domain internet access** — For SageMaker AI Studio, the following condition key may be used to disable internet access from the Studio domain:

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerPreventDirectInternetforStudio",
        "Effect": "Deny",
        "Action": "sagemaker:CreateDomain",
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "sagemaker:AppNetworkAccessType": [
              "PublicInternetOnly"
            ]
          }
        }
      }
    ]
  }
  ```

------

### Preventing privilege escalation
<a name="preventing-privilege-escalation"></a>
+ **Disabling SageMaker AI Notebook root access** — AWS recommends disabling the root access to SageMaker AI Notebooks for the data scientists and ML engineers. The following policy prevents a user from launching a SageMaker AI Notebook if `RootAccess` is not disabled.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerDenyRootAccess",
        "Effect": "Deny",
        "Action": [
          "sagemaker:CreateNotebookInstance",
          "sagemaker:UpdateNotebookInstance"
        ],
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "sagemaker:RootAccess": [
              "Enabled"
            ]
          }
        }
      }
    ]
  }
  ```

------

### Enforcing tags
<a name="enforcing-tags"></a>
+ **Requiring tag for API call in dev environment** - the following policy requires a “dev” environment tag to be attached to the SageMaker AI endpoint.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerRequireEnvTag",
        "Effect": "Deny",
        "Action": "sagemaker:CreateEndpoint",
        "Resource": "arn:aws:sagemaker:*:*:endpoint/*",
        "Condition": {
          "StringNotEquals": {
            "aws:RequestTag/environment": "dev"
          }
        }
      }
    ]
  }
  ```

------
+ **Requiring tag for Studio domains in data science accounts** - To ensure that administrators appropriately tag Studio domains, kernels, and notebooks on creation, you can use the following policy. For example, for developers in data science accounts inside an OU, a Studio created in these accounts should be tagged as follows.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Sid": "RequireAppTag",
              "Effect": "Deny",
              "Action": [
                  "sagemaker:CreateDomain"
              ],
              "Resource": "*",
              "Condition": {
                  "StringNotLike": {
                      "aws:RequestTag/Project": "data_science"
                  }
              }
          }
      ]
  }
  ```

------

### Controlling cost
<a name="controlling-cost"></a>
+ **Enforcing instance type for a SageMaker AI Notebook instance** — The following policy ensures that only the listed instances types can be used to create a notebook instance.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerLimitInstanceTypes",
        "Effect": "Deny",
        "Action": "sagemaker:CreateNotebookInstance",
        "Resource": "*",
        "Condition": {
          "ForAnyValue:StringNotLike": {
            "sagemaker:InstanceTypes": [
              "ml.c5.xlarge",
              "ml.m5.xlarge",
              "ml.t3.medium"
            ]
          }
        }
      }
    ]
  }
  ```

------
+ **Enforcing instance type for Studio Notebook instance** — The following policy helps enforce the type of instances used for SageMaker AI Studio notebook.

------
#### [ JSON ]

****

  ```
  {
    "Version":"2012-10-17",
    "Statement": [
      {
        "Sid": "SageMakerAllowedInstanceTypes",
        "Effect": "Deny",
        "Action": [
          "sagemaker:CreateApp"
        ],
        "Resource": "*",
        "Condition": {
          "ForAnyValue:StringNotLike": {
            "sagemaker:InstanceTypes": [
              "ml.c5.large",
              "ml.m5.large",
              "ml.t3.medium"
            ]
          }
        }
      }
    ]
  }
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
