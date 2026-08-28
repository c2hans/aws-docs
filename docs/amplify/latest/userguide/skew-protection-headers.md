---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection-headers.html
---

# How skew protection works
<a name="skew-protection-headers"></a>

In most cases, the default behavior of the \_dpl cookie will serve your skew protection needs. However, in the following advanced scenarios, skew protection is better enabled using the `X-Amplify-Dpl` header and `dpl` query parameter.
+ Loading your website in multiple browser tabs at the same time
+ Using service workers

Amplify evaluates the incoming request in the following order when determining the content to serve to the client:

1. **`X-Amplify-Dpl` header** – Applications can use this header to direct requests to a specific Amplify deployment. This request header can be set by using the value of `process.env.AWS_AMPLIFY_DEPLOYMENT_ID`.

1. **`dpl` query parameter** – Next.js applications will automatically set the \_dpl query parameter for requests to fingerprinted assets (.js and .css files).

1. **\_dpl cookie** – This is the default for all skew protected applications. For a specific browser, the same cookie is sent for every browser tab or instance that interacts with a domain.

   Be aware that if different browser tabs have different versions of a website loaded, the \_dpl cookie is shared by all of the tabs. In this scenario, it isn't possible to achieve total skew protection with the \_dpl cookie and you should consider using the `X-Amplify-Dpl` header for skew protection.

## X-Amplify-Dpl header example
<a name="skew-protection-header-example"></a>

The following example demonstrates the code for a Next.js SSR page that accesses skew protection through the `X-Amplify-Dpl` header. The page renders its content based on one of its api routes. The deployment to serve to the api route is specified by using the `X-Amplify-Dpl` header, that is set to the value of `process.env.AWS_AMPLIFY_DEPLOYMENT_ID`.

```
import { useEffect, useState } from 'react';

export default function MyPage({deploymentId}) {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('/api/hello', {
            headers: {
                'X-Amplify-Dpl': process.env.AWS_AMPLIFY_DEPLOYMENT_ID
            },
        })
        .then(res => res.json())
        .then(data => setData(data))
        .catch(error => console.error("error", error))
    }, []);

    return <div>
        {data ? JSON.stringify(data) : "Loading ... " }
    </div>
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
