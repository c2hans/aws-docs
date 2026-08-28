---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/sdk-acme-update-domain-validation.html
---

# Updating an ACME domain validation
<a name="sdk-acme-update-domain-validation"></a>

The following example shows how to use the [UpdateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateAcmeDomainValidation.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.UpdateAcmeDomainValidationRequest;
import com.amazonaws.services.certificatemanager.model.PrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DnsPrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DomainScope;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure updated domain scope.
        DomainScope domainScope = new DomainScope()
            .withExactDomain("ENABLED")
            .withSubdomains("DISABLED")
            .withWildcards("DISABLED");

        DnsPrevalidationOptions dnsOptions = new DnsPrevalidationOptions()
            .withDomainScope(domainScope);

        PrevalidationOptions prevalidationOptions = new PrevalidationOptions()
            .withDnsPrevalidation(dnsOptions);

        // Create the request.
        UpdateAcmeDomainValidationRequest req = new UpdateAcmeDomainValidationRequest()
            .withAcmeDomainValidationArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example/acme-domain-validation/dv-example")
            .withPrevalidationOptions(prevalidationOptions);

        // Update the domain validation.
        client.updateAcmeDomainValidation(req);
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
