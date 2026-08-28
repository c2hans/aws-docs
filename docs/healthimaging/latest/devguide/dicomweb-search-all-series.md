---
source_url: https://docs.aws.amazon.com/healthimaging/latest/devguide/dicomweb-search-all-series.html
---

# Searching for all DICOM series in HealthImaging
<a name="dicomweb-search-all-series"></a>

Use the `SearchDICOMAllSeries` API to search for all DICOM series across an HealthImaging [data store](getting-started-concepts.md#concept-data-store). Construct a request URL with supported DICOM data elements (attributes) to filter results. The API returns series search results in JSON format, ordered by `Series Number (0020,0011)` in ascending order (oldest to latest).

**To search for all DICOM series**

1. Collect HealthImaging `region` and `datastoreId` values. For more information, see [Getting data store properties](get-data-store.md).

1. Construct a URL for the request, including all applicable Series elements. The URL is of the form:

   ```
   GET https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/series[?query]
   ```

   The following table lists the supported DICOM data elements (attributes).
**Series elements for `SearchDICOMAllSeries`**
[See the AWS documentation website for more details](http://docs.aws.amazon.com/healthimaging/latest/devguide/dicomweb-search-all-series.html)

1. Prepare and send your request. `SearchDICOMAllSeries` uses an HTTP GET request signed with [AWS Signature Version 4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html). The following example uses the `curl` command-line tool. Replace `{{region}}` with your AWS Region. Replace `{{datastoreId}}` with your data store ID.

------
#### [ curl ]

   ```
   curl --request GET \
     "https://dicom-medical-imaging.{{region}}.amazonaws.com/datastore/{{datastoreId}}/series[?query]" \
     --aws-sigv4 'aws:amz:{{region}}:medical-imaging' \
     --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
     --header "x-amz-security-token:$AWS_SESSION_TOKEN" \
     --header 'Accept: application/dicom+json' \
     --output results.json
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
