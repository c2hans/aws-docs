---
name: ra-createsession-signer
description: Working Python implementation of the non-SDK Roles Anywhere CreateSession X.509 signing process, plus cert/CRL generators
metadata:
  type: reference
---

Roles Anywhere `CreateSession POST /sessions` is not in any SDK. A from-scratch working signer exists at:
- `/work/ra/createsession.py` — AWS4-X509-RSA-SHA256 signer (SigV4-like; Credential = decimal cert serial / date / region / rolesanywhere / aws4_request; signed headers content-type;host;x-amz-date;x-amz-x509; X-Amz-X509 = base64 DER of EE cert). Returns raw status/x-amzn-RequestId/body.
- `/work/ra/certs.py` — self-signed CA + EE cert generation (RSA-2048) via `cryptography`.
- `/work/ra/poll.py` — rapid CreateSession poller for TOCTOU/window measurement.

The official `aws_signing_helper` (github.com/aws/rolesanywhere-credential-helper) could NOT be `go install`ed — the Go module proxy at $PROXY_GATEWAY refused. Implementing the signer directly in Python was faster and gave better evidence (raw request IDs). Always run a positive-control CreateSession (honest cert + its own trust anchor) first to validate the signer before any crux/spoof test.

Note: `cryptography` API is `x509.load_pem_x509_certificate` (not `load_pem_certificate`).
