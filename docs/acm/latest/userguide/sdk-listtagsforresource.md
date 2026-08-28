---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/sdk-listtagsforresource.html
---

# Listing tags for a resource
<a name="sdk-listtagsforresource"></a>

The following example shows how to use the [ListTagsForResource](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForResource.html) function. This API supports all ACM resource types except the `certificate` resource type. For certificate resources, use [ListTagsForCertificate](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListTagsForCertificate.html).

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.ListTagsForResourceRequest;
import com.amazonaws.services.certificatemanager.model.ListTagsForResourceResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create a request object.
        ListTagsForResourceRequest req = new ListTagsForResourceRequest()
            .withResourceArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-abc123");

        // List the tags.
        ListTagsForResourceResult result = client.listTagsForResource(req);
        System.out.println(result);
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
