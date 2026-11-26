---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/envoy-admin-interface.html
---

# Use the Envoy admin interface securely

Envoy's admin interface is disabled unless your bootstrap configuration file includes an `admin` block. ELB for Envoy doesn't expose the admin interface for you. If you enable it, restrict access to the interface, because endpoints such as `/config_dump` can reveal secrets in your configuration.

Customer HTTP admin requests support only the `GET` and `HEAD` methods, and only on the paths listed in [Supported paths and methods](#envoy-admin-interface-paths).

Before you begin, make sure you have the following:
+ A proxy with a bootstrap configuration file that you can update. For more information, see [Update a proxy configuration](update-proxy-configuration.md).
+ Access to the security groups associated with the proxy.

**To enable and secure the admin interface**

1. In your bootstrap configuration file, add an `admin` block bound to the loopback address `127.0.0.1`. An admin interface bound to `127.0.0.1` isn't reachable from your VPC or the internet; only Envoy itself and the listeners that you define can reach it.

1.
**Warning**
Endpoints such as `/config_dump` can reveal secrets embedded in your configuration. Expose only the endpoints that you need, and limit access to trusted diagnostic clients.

   Expose only the endpoints that you need, through a listener that you control. Define a cluster that points at the admin address, and route only specific paths to it. This lets you add TLS, authentication filters, and security group rules in front of the admin endpoints, none of which the admin interface supports natively.

   The following example binds the admin interface to the loopback address and exposes only the Prometheus statistics endpoint, for scrapers, on port 19001.

   Fragment:

   ```
   admin:
     address:
       socket_address:
         address: 127.0.0.1
         port_value: 9901

   static_resources:
     listeners:
     - name: stats_listener
       address:
         socket_address:
           address: 0.0.0.0
           port_value: 19001
       filter_chains:
       - filters:
         - name: envoy.filters.network.http_connection_manager
           typed_config:
             "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
             stat_prefix: admin_stats
             http_filters:
             - name: envoy.filters.http.router
               typed_config:
                 "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
             route_config:
               name: admin_routes
               virtual_hosts:
               - name: admin_endpoints
                 domains: ["*"]
                 routes:
                 - match:
                     path: /stats/prometheus
                     headers:
                     - name: ":method"
                       string_match:
                         exact: GET
                   route:
                     cluster: admin_cluster

     clusters:
     - name: admin_cluster
       type: STATIC
       load_assignment:
         cluster_name: admin_cluster
         endpoints:
         - lb_endpoints:
           - endpoint:
               address:
                 socket_address:
                   address: 127.0.0.1
                   port_value: 9901
   ```

1. Add inbound security group rules that allow the listener port only from the hosts that need it. For the preceding example, allow port 19001 only from your scrapers. For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) in the *Amazon VPC User Guide*.

1. Reach the interface through the proxy's `internal-` DNS name, which resolves to private VPC IP addresses. For more information about proxy DNS names, see [DNS names](how-proxies-work.md#how-proxies-work-dns).

## Supported paths and methods
<a name="envoy-admin-interface-paths"></a>

The admin interface supports the `GET` and `HEAD` methods on the following paths.

| Path | Supported methods |
| --- | --- |
| /stats | GET, HEAD |
| /stats/prometheus | GET, HEAD |
| /clusters | GET, HEAD |
| /config\_dump | GET, HEAD |
| /ready | GET, HEAD |
| /listeners | GET, HEAD |

Other paths and methods, including `POST` to a supported path, return Envoy's unknown-path HTTP 404 response. Path matching is exact and excludes the query string: `/stats` doesn't enable `/stats/recentlookups` or its `/clear`, `/disable`, and `/enable` controls. The `/help` and `/` paths aren't available. Supported diagnostic query parameters remain available, including `/stats?format=json` and `/stats?format=prometheus`.

Your `admin.allow_paths` settings can further restrict these paths but can't add endpoints or methods. A supported `GET` or `HEAD` request that `admin.allow_paths` excludes receives HTTP 403; unsupported paths and methods still receive HTTP 404. To change log levels, use the `envoy.log_level` and `envoy.component_log_level` proxy attributes (see [Troubleshoot ELB for Envoy](troubleshooting.md)).
