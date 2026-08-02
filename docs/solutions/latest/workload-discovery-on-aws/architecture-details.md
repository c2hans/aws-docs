---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## Authentication mechanism
<a name="authentication-mechanism"></a>

Workload Discovery on AWS uses an [Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) for both the UI and AWS AppSync authentication. Once authenticated, Amazon Cognito provides a [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) (JWT) to the web UI that will be provided with all subsequent API requests. If a valid JWT is not provided, the API request will fail and return an HTTP 403 Forbidden response.

## Supported resources
<a name="supported-resources"></a>

For a list of AWS resource types that Workload Discovery on AWS can discover within your accounts and Regions, refer to [Supported resources.](supported-resources-1.md)

## Workload Discovery on AWS architecture diagram management
<a name="workload-discovery-on-aws-architecture-diagram-management"></a>

You can save Workload Discovery on AWS architecture diagrams using the web UI where create, read, update, and delete (CRUD) operations can be performed. The [AWS Amplify storage API](https://docs.amplify.aws/gen1/react/build-a-backend/storage/) allows Workload Discovery on AWS to store architecture diagrams in an Amazon S3 bucket. There are two levels of permissions available:
+  **All users** - Allows Workload Discovery on AWS architecture diagrams to be visible to Workload Discovery on AWS users in your deployment. Users can download and edit these diagrams.
+  **You** - Allows Workload Discovery on AWS architecture diagrams to be visible only to the creator. Other users will not be able to view them.
