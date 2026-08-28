---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/context-reference.html
---

# AWS AppSync Event API context reference
<a name="context-reference"></a>

AWS AppSync defines a set of variables and functions for working with handlers. This topic describes these functions and provides examples.

## Accessing the `context`
<a name="accessing-the-context"></a>

The `context` argument of a request and response handler is an object that holds all of the contextual information for your handler invocation. It has the following structure:

```
type Context = {
  identity?: Identity;
  result?: any;
  request: Request;
  info: EventsInfo;
  stash: any;
  error?: Error
  events?: IncomingEvent[];
}
```

**Note**
The `context` object is commonly referred to as `ctx`.

Each field in the `context` object is defined as follows:

### `context` fields
<a name="accessing-the-context-list"></a>

** `identity` **
An object that contains information about the caller. For more information about the structure of this field, see [Identity](#context-reference-identity).

** `result` **
A container for the results of this handler when a data source is configured, available in the response function of a namespace handler.

** `request` **
A container for the headers and information about the custom domain that was used.

** `info` **
An object that contains information about the operation on the channel namespace. For the structure of this field, see [Info](#info-property).

** `stash` **
The stash is an object that is made available inside each handler. The same stash object lives through a single handler evaluation. You can use the stash to pass arbitrary data across request and response functions of your handlers.
You can add items to the stash as follows:

```
ctx.stash.newItem = { key: "something" }
Object.assign(ctx.stash, {key1: value1, key2: value})
```
You can remove items from the stash by modifying the following code:

```
delete ctx.stash.key
```

### Identity
<a name="context-reference-identity"></a>

The `identity` section contains information about the caller. The shape of this section depends on the authorization type of your AWS AppSync API. For more information about security options, see [Configuring authorization and authentication to secure Event APIs](configure-event-api-auth.md).

** `API_KEY` authorization**
The `identity` field isn't populated.

**`AWS_LAMBDA` authorization**
The `identity` has the following form:

```
type AppSyncIdentityLambda = {
  handlerContext: any;
};
```
The `identity` contains the `handlerContext` key, containing the same `handlerContext` content returned by the Lambda function authorizing the request.

** `AWS_IAM` authorization**
The `identity` has the following form:

```
type AppSyncIdentityIAM = {
  accountId: string;
  cognitoIdentityPoolId: string;
  cognitoIdentityId: string;
  sourceIp: string[];
  username: string;
  userArn: string;
  cognitoIdentityAuthType: string;
  cognitoIdentityAuthProvider: string;
};
```

** `AMAZON_COGNITO_USER_POOLS` authorization**
The `identity` has the following form:

```
type AppSyncIdentityCognito = {
  sourceIp: string[];
  username: string;
  groups: string[] | null;
  sub: string;
  issuer: string;
  claims: any;
  defaultAuthStrategy: string;
};
```

Each field is defined as follows:

** `accountId` **
The AWS account ID of the caller.

** `claims` **
The claims that the user has.

** `cognitoIdentityAuthType` **
Either authenticated or unauthenticated based on the identity type.

** `cognitoIdentityAuthProvider` **
A comma-separated list of external identity provider information used in obtaining the credentials used to sign the request.

** `cognitoIdentityId` **
The Amazon Cognito identity ID of the caller.

** `cognitoIdentityPoolId` **
The Amazon Cognito identity pool ID associated with the caller.

** `defaultAuthStrategy` **
The default authorization strategy for this caller (`ALLOW` or `DENY`).

** `issuer` **
The token issuer.

** `sourceIp` **
The source IP address of the caller that AWS AppSync receives. If the request doesn't include the `x-forwarded-for` header, the source IP value contains only a single IP address from the TCP connection. If the request includes a `x-forwarded-for` header, the source IP is a list of IP addresses from the `x-forwarded-for` header, in addition to the IP address from the TCP connection.

** `sub` **
The UUID of the authenticated user.

** `user` **
The IAM user.

** `userArn` **
The Amazon Resource Name (ARN) of the IAM user.

** `username` **
The user name of the authenticated user. In the case of `AMAZON_COGNITO_USER_POOLS` authorization, the value of *username* is the value of attribute *cognito:username*. In the case of `AWS_IAM` authorization, the value of *username* is the value of the AWS user principal. If you're using IAM authorization with credentials vended from Amazon Cognito identity pools, we recommend that you use `cognitoIdentityId`.

### Request property
<a name="request-property"></a>

The `request` property contains the headers that were sent with the request, and the custom domain name if it was used.

**Request headers**

The headers sent in HTTP requests to your API.

AWS AppSync supports passing custom headers from clients and accessing them in your handlers by using `ctx.request.headers`. You can then use the header values for actions such as inserting data into a data source or authorization checks. You can use single or multiple request headers.

If you set a header of `animal` with a value of `duck` as in the following example:

```
curl --location "https://YOUR_EVENT_API_ENDPOINT/event" \
--header 'Content-Type: application/json' \
--header "x-api-key:ABC123" \
--header "animal:duck" \
--data '{ "channel":"/news", "events":["\"Breaking news!\""] }'
```

Then, this could then be accessed with `ctx.request.headers.animal`.

You can also pass multiple headers in a single request and access these in the handler. For example, if the `custom` header is set with two values as follows:

```
curl --location "https://YOUR_EVENT_API_ENDPOINT/event" \
--header 'Content-Type: application/json' \
--header "x-api-key:ABC123" \
--header "animal:duck" \
--header "animal:goose" \
--data '{ "channel":"/news", "events":["\"Breaking news!\""] }'
```

You could then access these as an array, such as `ctx.request.headers.animal[1]`.

**Note**
AWS AppSync doesn't expose the cookie header in `ctx.request.headers`.

**Access the request custom domain name**

AWS AppSync supports configuring a custom domain that you can use to access your HTTP and WebSocket real-time endpoints for your APIs. When making a request with a custom domain name, you can get the domain name using `ctx.request.domainName`. When using the default endpoint domain name, the value is `null`.

### Info property
<a name="info-property"></a>

The `info` section contains information about the request made to your channel namespace. This section has the following form:

```
type EventsInfo = {
  info: {
    channel: {
      path: string;
      segments: string[];
    }
  };
  channelNamespace: {
    name: string
  }
  operation: 'SUBSCRIBE' | 'PUBLISH'
}
```

Each field is defined as follows:

** `info.channel.path` **
The channel path the operation is executed on, for example, `/default/user/johm`.

** `info.channel.segments` **
The segments of the channel path, for example, `['default', 'user', 'john']`.

** `info.channelNamespace.name` **
The name of the channel namespace, for example, `'default'`.

** `info.operation ` **
The operation executed: `PUBLISH` or `SUBSCRIBE`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
