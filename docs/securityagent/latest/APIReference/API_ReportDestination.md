---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ReportDestination.html
---

# ReportDestination
<a name="API_ReportDestination"></a>

Destination for publishing scan reports to an integrated document provider.

## Contents
<a name="API_ReportDestination_Contents"></a>

 ** containerId **   <a name="securityagent-Type-ReportDestination-containerId"></a>
The container identifier where the report will be published.
Type: String
Required: Yes

 ** integrationId **   <a name="securityagent-Type-ReportDestination-integrationId"></a>
The integration identifier for the document provider.
Type: String
Required: Yes

 ** documentId **   <a name="securityagent-Type-ReportDestination-documentId"></a>
The existing document identifier to update instead of creating a new document.
Type: String
Required: No

 ** parentId **   <a name="securityagent-Type-ReportDestination-parentId"></a>
The parent document identifier under which the report will be created.
Type: String
Required: No

## See Also
<a name="API_ReportDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ReportDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ReportDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ReportDestination)
