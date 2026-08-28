---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_FormTypeData.html
---

# FormTypeData
<a name="API_FormTypeData"></a>

The details of the metadata form type.

## Contents
<a name="API_FormTypeData_Contents"></a>

 ** domainId **   <a name="datazone-Type-FormTypeData-domainId"></a>
The identifier of the Amazon DataZone domain in which the form type exists.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-FormTypeData-name"></a>
The name of the form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*`
Required: Yes

 ** revision **   <a name="datazone-Type-FormTypeData-revision"></a>
The revision of the form type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** createdAt **   <a name="datazone-Type-FormTypeData-createdAt"></a>
The timestamp of when the metadata form type was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-FormTypeData-createdBy"></a>
The Amazon DataZone user who created teh metadata form type.
Type: String
Required: No

 ** description **   <a name="datazone-Type-FormTypeData-description"></a>
The description of the metadata form type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** imports **   <a name="datazone-Type-FormTypeData-imports"></a>
The imports specified in the form type.
Type: Array of [Import](API_Import.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** model **   <a name="datazone-Type-FormTypeData-model"></a>
The model of the form type.
Type: [Model](API_Model.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** originDomainId **   <a name="datazone-Type-FormTypeData-originDomainId"></a>
The identifier of the Amazon DataZone domain in which the form type was originally created.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** originProjectId **   <a name="datazone-Type-FormTypeData-originProjectId"></a>
The identifier of the project in which the form type was originally created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** owningProjectId **   <a name="datazone-Type-FormTypeData-owningProjectId"></a>
The identifier of the project that owns the form type.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** status **   <a name="datazone-Type-FormTypeData-status"></a>
The status of the form type.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_FormTypeData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/FormTypeData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/FormTypeData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/FormTypeData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
