---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ProjectPolicyGrantPrincipal.html
---

# ProjectPolicyGrantPrincipal
<a name="API_ProjectPolicyGrantPrincipal"></a>

The project policy grant principal.

## Contents
<a name="API_ProjectPolicyGrantPrincipal_Contents"></a>

 ** projectDesignation **   <a name="datazone-Type-ProjectPolicyGrantPrincipal-projectDesignation"></a>
The project designation of the project policy grant principal.
Type: String
Valid Values: `OWNER | CONTRIBUTOR | PROJECT_CATALOG_STEWARD`
Required: Yes

 ** projectGrantFilter **   <a name="datazone-Type-ProjectPolicyGrantPrincipal-projectGrantFilter"></a>
The project grant filter of the project policy grant principal.
Type: [ProjectGrantFilter](API_ProjectGrantFilter.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** projectIdentifier **   <a name="datazone-Type-ProjectPolicyGrantPrincipal-projectIdentifier"></a>
The project ID of the project policy grant principal.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_ProjectPolicyGrantPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ProjectPolicyGrantPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ProjectPolicyGrantPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ProjectPolicyGrantPrincipal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
