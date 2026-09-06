---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SingleSignOn.html
---

# SingleSignOn
<a name="API_SingleSignOn"></a>

The single sign-on details in Amazon DataZone.

## Contents
<a name="API_SingleSignOn_Contents"></a>

 ** idcInstanceArn **   <a name="datazone-Type-SingleSignOn-idcInstanceArn"></a>
The ARN of the IDC instance.
Type: String
Pattern: `.*arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}.*`
Required: No

 ** type **   <a name="datazone-Type-SingleSignOn-type"></a>
The type of single sign-on in Amazon DataZone.
Type: String
Valid Values: `IAM_IDC | DISABLED`
Required: No

 ** userAssignment **   <a name="datazone-Type-SingleSignOn-userAssignment"></a>
The single sign-on user assignment in Amazon DataZone.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: No

## See Also
<a name="API_SingleSignOn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SingleSignOn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SingleSignOn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SingleSignOn)
