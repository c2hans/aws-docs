---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateOutput.html
---

# UpdateOutput
<a name="API_UpdateOutput"></a>

Contains configuration information about one output in a feed. It is used in the UpdateFeed action.

## Contents
<a name="API_UpdateOutput_Contents"></a>

 ** name **   <a name="elementalinference-Type-UpdateOutput-name"></a>
The name of the output.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** outputConfig **   <a name="elementalinference-Type-UpdateOutput-outputConfig"></a>
A typed property for an output in a feed. It identifies the action for Elemental Inference to perform. It also provides a repository for the results of that action. For example, CroppingConfig output will contain the metadata for the crop feature.
Type: [OutputConfig](API_OutputConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** status **   <a name="elementalinference-Type-UpdateOutput-status"></a>
The status of the output.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** description **   <a name="elementalinference-Type-UpdateOutput-description"></a>
A description of the output.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\w \-\.',@:;]*`
Required: No

 ** fromAssociation **   <a name="elementalinference-Type-UpdateOutput-fromAssociation"></a>
Elemental Inference originally sets this parameter to True if this output was created by AssociateFeed or to False if this output was created by CreateFeed or UpdateFeed.
You must not change this value. Therefore, use GetFeed to determine the current value. Then in the UpdateFeed request, if the current value is True, include this parameter with a value of True. If it's False, omit the parameter.
Type: Boolean
Required: No

## See Also
<a name="API_UpdateOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/UpdateOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/UpdateOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/UpdateOutput)
