---
name: bedrock-kb-ssrf-testing
description: How to stand up a Bedrock Knowledge Base for SSRF/fetcher testing, and the containments that held (finding 16)
metadata:
  type: reference
---

Testing Amazon Bedrock Knowledge Base managed fetchers (web crawler + Salesforce/Confluence/SharePoint connectors) for SSRF. See `/work/findings/16-bedrock-kb-ssrf-webcrawler-contained.md`.

**Setup facts (save hours):**
- WEB and credentialed-connector data sources REQUIRE an OpenSearch Serverless (OSS) backing store. S3 Vectors / other stores are rejected with `ValidationException: ... only supported for ... OpenSearch Serverless`.
- OSS data-plane SigV4 (creating the vector index, `_search`) needs the `X-Amz-Content-SHA256` header set to the body hash BEFORE signing, or writes 403 while reads 404/200. botocore SigV4Auth does NOT add it for aoss.
- KB role needs IAM `aoss:APIAccessAll` on the collection AND the role ARN listed in the OSS data-access policy. Bedrock's storage-config validation 403s intermittently on IAM/aoss propagation — retry with backoff.
- Cheapest control-plane oracle for crawl outcomes: enable KB CloudWatch application-log delivery (`logs:PutDeliverySource`/`PutDeliveryDestination`/`CreateDelivery`) — gives per-URL `status`/`status_reasons` (RESOURCE_CRAWLED / RESOURCE_IGNORED / robots skip / scope skip). Ingestion-job `failureReasons` also carries these.
- Only ONE ingestion job per KB at a time; max 5 data sources per KB — run the battery sequentially / in waves.
- Best egress oracle: your own Lambda+API-GW HTTP responder logs source IP + UA + headers + body directly (self-contained, no interactsh dependency). Crawler UA is `bedrockbot_<UUID>`, egress from AWS EC2 ranges (e.g. 34.224.0.0/12 us-east-1).

**Containments that held (verdict REFUTED for the dangerous vectors):**
- Web crawler fetches customer seed URLs from AWS egress and content IS readable back (Retrieve / OSS _search).
- Control plane ACCEPTS link-local/loopback/RFC1918 seed URLs (regex `https?://[A-Za-z0-9][^\s]*`) — but runtime yields 0 content: direct internal seed -> "robots.txt disallows"; it enforces robots.txt (RFC9309, disallow-by-default).
- Redirect targets are RE-VALIDATED against crawl scope: off-host/cross-host 302 -> "redirected to a content location outside of the specified scope"; 302 to link-local -> "internal server issue", 0 indexed.
- Connectors validate the destination is the expected SaaS vendor domain (*.salesforce.com / *.atlassian.net) BEFORE any fetch -> credential-forwarding (P4) refused, no cred left AWS.
