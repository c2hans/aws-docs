---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_View.html
---

# View
<a name="API_connect-participant_View"></a>

A view resource object. Contains metadata and content necessary to render the view.

## Contents
<a name="API_connect-participant_View_Contents"></a>

 ** Arn **   <a name="connect-Type-connect-participant_View-Arn"></a>
The Amazon Resource Name (ARN) of the view.
Type: String
Required: No

 ** Content **   <a name="connect-Type-connect-participant_View-Content"></a>
View content containing all content necessary to render a view except for runtime input data.
Type: [ViewContent](API_connect-participant_ViewContent.md) object
Required: No

 ** Id **   <a name="connect-Type-connect-participant_View-Id"></a>
The identifier of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^[a-zA-Z0-9\_\-:\/$]+$`
Required: No

 ** Name **   <a name="connect-Type-connect-participant_View-Name"></a>
The name of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()']*)$`
Required: No

 ** Version **   <a name="connect-Type-connect-participant_View-Version"></a>
The current version of the view.
Type: Integer
Required: No

## See Also
<a name="API_connect-participant_View_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/View)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/View)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/View)
