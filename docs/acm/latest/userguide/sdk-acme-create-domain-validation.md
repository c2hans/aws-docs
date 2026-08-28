---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/sdk-acme-create-domain-validation.html
---

# Creating an ACME domain validation
<a name="sdk-acme-create-domain-validation"></a>

The following example shows how to use the [CreateAcmeDomainValidation](https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeDomainValidation.html) function.

```
package com.amazonaws.samples;

import com.amazonaws.services.certificatemanager.AWSCertificateManagerClientBuilder;
import com.amazonaws.services.certificatemanager.AWSCertificateManager;
import com.amazonaws.services.certificatemanager.model.CreateAcmeDomainValidationRequest;
import com.amazonaws.services.certificatemanager.model.CreateAcmeDomainValidationResult;
import com.amazonaws.services.certificatemanager.model.PrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DnsPrevalidationOptions;
import com.amazonaws.services.certificatemanager.model.DomainScope;

public class AWSCertificateManagerSample {

    public static void main(String[] args) {

        AWSCertificateManager client = AWSCertificateManagerClientBuilder.defaultClient();

        // Configure domain scope.
        DomainScope domainScope = new DomainScope()
            .withExactDomain("ENABLED")
            .withSubdomains("ENABLED")
            .withWildcards("ENABLED");

        // Configure DNS prevalidation options.
        DnsPrevalidationOptions dnsOptions = new DnsPrevalidationOptions()
            .withDomainScope(domainScope)
            .withHostedZoneId("Z1234567890");

        PrevalidationOptions prevalidationOptions = new PrevalidationOptions()
            .withDnsPrevalidation(dnsOptions);

        // Create the request.
        CreateAcmeDomainValidationRequest req = new CreateAcmeDomainValidationRequest()
            .withAcmeEndpointArn("arn:aws:acm:us-east-1:123456789012:acme-endpoint/ep-example")
            .withDomainName("example.com")
            .withPrevalidationOptions(prevalidationOptions);

        // Create the domain validation.
        CreateAcmeDomainValidationResult result = client.createAcmeDomainValidation(req);
        System.out.println(result.getAcmeDomainValidationArn());
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
