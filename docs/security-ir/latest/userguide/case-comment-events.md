---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/case-comment-events.html
---

# Case Comment Events
<a name="case-comment-events"></a>

Case Comment Added by AWS Responder

```
            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Comment Added",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T04:30:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "createdBy": "AWS Responder"
              }
            }
```

Case Comment Added by Customer

```
            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Comment Added",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T02:15:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "createdBy": "111122223333"
              }
            }
```

Case Comment Added by AWS Security Incident Response Service

```
            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Comment Added",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T02:15:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "createdBy": "security-ir.amazonaws.com"
              }
            }
```

Case Comment Updated by Customer

```
            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Comment Updated",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T02:45:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "updatedBy": "111122223333"
              }
            }
```

Case Comment Updated by AWS Security Incident Response Service

```
            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Comment Updated",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T02:45:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "updatedBy": "security-ir.amazonaws.com"
              }
            }
```

Case Comment Updated by AWS Responder

```
            {
              "version": "0",
              "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
              "detail-type": "Case Comment Updated",
              "source": "aws.security-ir",
              "account": "111122223333",
              "time": "2023-05-12T02:45:00Z",
              "region": "us-west-2",
              "resources": [
                "arn:aws:security-ir:us-west-2:111122223333:case/1234567890"
              ],
              "detail": {
                "caseId": "1234567890",
                "updatedBy": "AWS Responder"
              }
            }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
