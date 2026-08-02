---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Asg.html
---

# Asg
<a name="API_Asg"></a>

Configuration for an Amazon EC2 Auto Scaling group used in a Region switch plan.

## Contents
<a name="API_Asg_Contents"></a>

 ** arn **   <a name="regionswitch-Type-Asg-arn"></a>
The Amazon Resource Name (ARN) of the EC2 Auto Scaling group.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:autoscaling:[a-z0-9-]+:\d{12}:autoScalingGroup:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}:autoScalingGroupName/[\S\s]{1,255}`
Required: No

 ** crossAccountRole **   <a name="regionswitch-Type-Asg-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-Asg-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

## See Also
<a name="API_Asg_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Asg)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Asg)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Asg)
