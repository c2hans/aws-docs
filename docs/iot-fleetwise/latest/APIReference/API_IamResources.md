---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_IamResources.html
---

# IamResources
<a name="API_IamResources"></a>

The IAM resource that enables AWS IoT FleetWise edge agent software to send data to Amazon Timestream.

For more information, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the * AWS Identity and Access Management User Guide*.

## Contents
<a name="API_IamResources_Contents"></a>

 ** roleArn **   <a name="iotfleetwise-Type-IamResources-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM resource that allows AWS IoT FleetWise to send data to Amazon Timestream. For example, `arn:aws:iam::123456789012:role/SERVICE-ROLE-ARN`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

## See Also
<a name="API_IamResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/IamResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/IamResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/IamResources)
