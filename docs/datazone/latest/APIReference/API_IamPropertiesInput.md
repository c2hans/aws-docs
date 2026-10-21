---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_IamPropertiesInput.html
---

# IamPropertiesInput
<a name="API_IamPropertiesInput"></a>

The IAM properties of a connection.

## Contents
<a name="API_IamPropertiesInput_Contents"></a>

 ** glueLineageSyncEnabled **   <a name="datazone-Type-IamPropertiesInput-glueLineageSyncEnabled"></a>
Specifies whether AWS Glue lineage sync is enabled for a connection.
Type: Boolean
Required: No

 ** roleArn **   <a name="datazone-Type-IamPropertiesInput-roleArn"></a>
The ARN of the IAM role to associate with the connection as the project user role. To use this operation, you must have `iam:PassRole` permission for this role.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:role(/[a-zA-Z0-9+=,.@_-]+)*/[a-zA-Z0-9+=,.@_-]+`
Required: No

## See Also
<a name="API_IamPropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/IamPropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/IamPropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/IamPropertiesInput)
