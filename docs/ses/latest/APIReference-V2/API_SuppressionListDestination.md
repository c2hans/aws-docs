---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SuppressionListDestination.html
---

# SuppressionListDestination
<a name="API_SuppressionListDestination"></a>

An object that contains details about the action of suppression list.

## Contents
<a name="API_SuppressionListDestination_Contents"></a>

 ** SuppressionListImportAction **   <a name="SES-Type-SuppressionListDestination-SuppressionListImportAction"></a>
The type of action to perform on the address. The following are possible values:
+ PUT: add the addresses to the suppression list. If the record already exists, it will override it with the new value.
+ DELETE: remove the addresses from the suppression list.
Type: String
Valid Values: `DELETE | PUT`
Required: Yes

## See Also
<a name="API_SuppressionListDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SuppressionListDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SuppressionListDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SuppressionListDestination)
