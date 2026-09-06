---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentActionSummary.html
---

# EnvironmentActionSummary
<a name="API_EnvironmentActionSummary"></a>

The details about the specified action configured for an environment. For example, the details of the specified console links for an analytics tool that is available in this environment.

## Contents
<a name="API_EnvironmentActionSummary_Contents"></a>

 ** domainId **   <a name="datazone-Type-EnvironmentActionSummary-domainId"></a>
The Amazon DataZone domain ID of the environment action.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** environmentId **   <a name="datazone-Type-EnvironmentActionSummary-environmentId"></a>
The environment ID of the environment action.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-EnvironmentActionSummary-id"></a>
The ID of the environment action.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-EnvironmentActionSummary-name"></a>
The name of the environment action.
Type: String
Required: Yes

 ** parameters **   <a name="datazone-Type-EnvironmentActionSummary-parameters"></a>
The parameters of the environment action.
Type: [ActionParameters](API_ActionParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** description **   <a name="datazone-Type-EnvironmentActionSummary-description"></a>
The environment action description.
Type: String
Required: No

## See Also
<a name="API_EnvironmentActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentActionSummary)
