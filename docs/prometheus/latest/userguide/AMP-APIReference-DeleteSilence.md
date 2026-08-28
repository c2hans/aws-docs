---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-DeleteSilence.html
---

# DeleteAlertManagerSilence
<a name="AMP-APIReference-DeleteSilence"></a>

The `DeleteSilence` deletes one alert silence.

Valid HTTP verbs:
`DELETE`

Valid URIs:
`/workspaces/{{workspaceId}}/alertmanager/api/v2/silence/{{silenceID}}`

URL query parameters: none

**Sample request**

```
DELETE /workspaces/ws-b226cc2a-a446-46a9-933a-ac50479a5568/alertmanager/api/v2/silence/d29d9df3-9125-4441-912c-70b05f86f973 HTTP/1.1
Content-Length: 0,
Authorization: AUTHPARAMS
X-Amz-Date: 20201201T193725Z
User-Agent: Grafana/8.1.0
```

**Sample response**

```
HTTP/1.1 200 OK
x-amzn-RequestId: 12345678-abcd-4442-b8c5-262b45e9b535
Content-Length: 0
Connection: keep-alive
Date: Tue, 01 Dec 2020 19:37:25 GMT
Content-Type: application/json
Server: amazon
vary: Origin
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
