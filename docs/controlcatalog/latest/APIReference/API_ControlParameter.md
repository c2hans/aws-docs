---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ControlParameter.html
---

# ControlParameter
<a name="API_ControlParameter"></a>

Five types of control parameters are supported.
+  **AllowedRegions**: List of AWS Regions exempted from the control. Each string is expected to be an AWS Region code. This parameter is mandatory for the **OU Region deny** control, **CT.MULTISERVICE.PV.1**.

  Example: `["us-east-1","us-west-2"]`
+  **ExemptedActions**: List of AWS IAM actions exempted from the control. Each string is expected to be an IAM action.

  Example: `["logs:DescribeLogGroups","logs:StartQuery","logs:GetQueryResults"]`
+  **ExemptedPrincipalArns**: List of AWS IAM principal ARNs exempted from the control. Each string is expected to be an IAM principal that follows the format `arn:partition:service::account:resource`

  Example: `["arn:aws:iam::*:role/ReadOnly","arn:aws:sts::*:assumed-role/ReadOnly/*"]`
+  **ExemptedResourceArns**: List of resource ARNs exempted from the control. Each string is expected to be a resource ARN.

  Example: `["arn:aws:s3:::my-bucket-name"]`
+  **ExemptAssumeRoot**: A parameter that lets you choose whether to exempt requests made with `AssumeRoot` from this control, for this OU. For member accounts, the `AssumeRoot` property is included in requests initiated by IAM centralized root access. This parameter applies only to the `AWS-GR_RESTRICT_ROOT_USER` control. If you add the parameter when enabling the control, the `AssumeRoot` exemption is allowed. If you omit the parameter, the `AssumeRoot` exception is not permitted. The parameter does not accept `False` as a value.

   *Example: Enabling the control and allowing `AssumeRoot` *

   `{ "controlIdentifier": "arn:aws:controlcatalog:::control/5kvme4m5d2b4d7if2fs5yg2ui", "parameters": [ { "key": "ExemptAssumeRoot", "value": true } ], "targetIdentifier": "arn:aws:organizations::8633900XXXXX:ou/o-6jmn81636m/ou-qsah-jtiihcla" }`

## Contents
<a name="API_ControlParameter_Contents"></a>

 ** Name **   <a name="controlcatalog-Type-ControlParameter-Name"></a>
The parameter name. This name is the parameter `key` when you call [`EnableControl`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_EnableControl.html) or [`UpdateEnabledControl`](https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateEnabledControl.html).
Type: String
Required: Yes

## See Also
<a name="API_ControlParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ControlParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ControlParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ControlParameter)
