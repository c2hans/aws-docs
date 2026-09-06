---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/idempotency.html
---

# Preventing duplicate jobs
<a name="idempotency"></a>

You can use *client request tokens* to ensure that a `create-job` API request completes only once. With these requests, if the original request completes successfully, subsequent requests have no additional effect. This is useful to prevent duplicate jobs from being created when you interact with the AWS Elemental MediaConvert API.

A client request token is a unique string that you specify when you make a create job request.

A client request token can be any string that includes up to 64 ASCII characters. If you reuse a client request token within one minute of a successful request, the API returns the job details of the original request instead.

**The following AWS CLI command creates an idempotent CreateJob request with the client request token {{example-token}}**.

```
aws mediaconvert create-job \
    --client-request-token {{example-token}} \
    --region {{region-name-1}} \
    --cli-input-json file://{{job.json}}
```

For more information about how to create a job using the AWS CLI, see the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job.html).
