---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/opensearch-function-reference.html
---

# AWS AppSync JavaScript function reference for Amazon OpenSearch Service
<a name="opensearch-function-reference"></a>

The AWS AppSync integration for Amazon OpenSearch Service enables you to store and retrieve data in existing OpenSearch Service domains in your account. This handler works by allowing you to create OpenSearch Service requests, and then map the OpenSearch Service response back to your application. This section describes the function request and response handlers for the supported OpenSearch Service operations.

## Request
<a name="request-js"></a>

Most OpenSearch Service request objects have a common structure where just a few pieces change. The following example runs a search against an OpenSearch Service domain, where documents are of type `post` and are indexed under `id`. The search parameters are defined in the `body` section, with many of the common query clauses being defined in the `query` field. This example will search for documents containing `"Nadia"`, or `"Bailey"`, or both, in the `author` field of a document:

```
export const onPublish = {
  request(ctx) {
    return {
      operation: 'GET',
      path: '/id/post/_search',
      params: {
        headers: {},
        queryString: {},
        body: {
          from: 0,
          size: 50,
          query: {
            bool: {
              should: [
                { match: { author: 'Nadia' } },
                { match: { author: 'Bailey' } },
              ],
            },
          },
        },
      },
    };
  }
}
```

## Response
<a name="response-js"></a>

As with other data sources, OpenSearch Service sends a response to AWS AppSync that needs to be processed. .

Most applications are looking for the `_source` field from an OpenSearch Service response. Because you can do searches to return either an individual document or a list of documents, there are two common response patterns used in OpenSearch Service.

 **List of Results**

```
export const onPublish = {
  response(ctx) {
    const entries = [];
    for (const entry of ctx.result.hits.hits) {
      entries.push(entry['_source']);
    }
  }
}
```

 **Individual Item**

```
export const onPublish = {
  response(ctx) {
    const result =  ctx.result['_source']
  }
}
```

## `operation` field
<a name="operation-field"></a>

**Note**
This applies only to the Request handler.

HTTP method or verb (GET, POST, PUT, HEAD or DELETE) that AWS AppSync sends to the OpenSearch Service domain. Both the key and the value must be a string.

```
"operation" : "PUT"
```

## `path` field
<a name="path-field"></a>

**Note**
This applies only to the Request handler.

The search path for an OpenSearch Service request from AWS AppSync. This forms a URL for the operation’s HTTP verb. Both the key and the value must be strings.

```
"path" : "/indexname/type"

"path" : "/indexname/type/_search"
```

When the request handler is evaluated, this path is sent as part of the HTTP request, including the OpenSearch Service domain. For example, the previous example might translate to:

```
GET https://opensearch-domain-name.REGION.es.amazonaws.com/indexname/type/_search
```

## `params` field
<a name="params-field"></a>

**Note**
This applies only to the Request handler.

Used to specify what action your search performs, most commonly by setting the **query** value inside of the **body**. However, there are several other capabilities that can be configured, such as the formatting of responses.
+  **headers**

  The header information, as key-value pairs. Both the key and the value must be strings. For example:

  ```
  "headers" : {
      "Content-Type" : "application/json"
  }
  ```

**Note**
AWS AppSync currently supports only JSON as a `Content-Type`.
+  **queryString**

  Key-value pairs that specify common options, such as code formatting for JSON responses. Both the key and the value must be a string. For example, if you want to get pretty-formatted JSON, you would use:

  ```
  "queryString" : {
      "pretty" : "true"
  }
  ```
+  **body**

  This is the main part of your request, allowing AWS AppSync to craft a well-formed search request to your OpenSearch Service domain. The key must be a string comprised of an object. A couple of demonstrations are shown below.

 **Example 1**

Return all documents with a city matching “seattle”:

```
export const onSubscribe = {
  request(ctx) {
    return {
      operation: 'GET',
      path: '/id/post/_search',
      params: {
        headers: {},
        queryString: {},
        body: { from: 0, size: 50, query: { match: { city: 'seattle' } } },
      },
    };
  }
}
```

 **Example 2**

Return all documents matching “washington” as the city or the state:

```
export const onSubscribe = {
  request(ctx) {
    return {
      operation: 'GET',
      path: '/id/post/_search',
      params: {
        headers: {},
        queryString: {},
        body: {
          from: 0,
          size: 50,
          query: {
            multi_match: { query: 'washington', fields: ['city', 'state'] },
          },
        },
      },
    };
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
