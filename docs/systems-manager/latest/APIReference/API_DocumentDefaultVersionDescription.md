---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentDefaultVersionDescription.html
---

# DocumentDefaultVersionDescription
<a name="API_DocumentDefaultVersionDescription"></a>

A default version of a document.

## Contents
<a name="API_DocumentDefaultVersionDescription_Contents"></a>

 ** DefaultVersion **   <a name="systemsmanager-Type-DocumentDefaultVersionDescription-DefaultVersion"></a>
The default version of the document.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** DefaultVersionName **   <a name="systemsmanager-Type-DocumentDefaultVersionDescription-DefaultVersionName"></a>
The default version of the artifact associated with the document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

 ** Name **   <a name="systemsmanager-Type-DocumentDefaultVersionDescription-Name"></a>
The name of the document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

## See Also
<a name="API_DocumentDefaultVersionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentDefaultVersionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentDefaultVersionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentDefaultVersionDescription)
