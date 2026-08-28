---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/sdk-acme-describe-eab.html
---

# Describing an ACME external account binding
<a name="sdk-acme-describe-eab"></a>

The following example shows how to use the [DescribeAcmeExternalAccountBinding](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeExternalAccountBinding.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.DescribeAcmeExternalAccountBindingRequest;
import com.amazonaws.services.certificatemanager.model.DescribeAcmeExternalAccountBindingResult;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Create the request.
        DescribeAcmeExternalAccountBindingRequest req = new DescribeAcmeExternalAccountBindingRequest()
            .withAcmeExternalAccountBindingArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example/acme-external-account-binding/eab-example");

        // Describe the external account binding.
        DescribeAcmeExternalAccountBindingResult result = client.describeAcmeExternalAccountBinding(req);
        System.out.println(result);
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
