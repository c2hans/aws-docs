---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/envoy-limits.html
---

# Envoy configuration limits and unsupported features

This section lists the limits that ELB for Envoy applies to your Envoy configuration, the restrictions on Lua scripts, and the Envoy features that ELB for Envoy does not support.

**Topics**
+ [General limits](#envoy-limits-general)
+ [Lua restrictions](#envoy-limits-lua)
+ [Unsupported features](#envoy-limits-unsupported)

## General limits
<a name="envoy-limits-general"></a>

ELB for Envoy limits the size of your configuration file and configuration archive, and the number of entries in the archive. For these values, see [Quotas for Elastic Load Balancing for Envoy](quotas.md).

The following general limits also apply:
+ You can select only an Envoy version in the currently supported set, and ELB for Envoy validates your configuration against that version's schema.
+ Schema acceptance does not guarantee that every extension is available. The ELB for Envoy Envoy build might not include every extension that the schema describes. In that case, your configuration fails at the `envoy --mode validate` stage rather than at the API.
+ The connection draining period is fixed at 60 seconds. If you issue a configuration update while a previous update is still draining, ELB for Envoy terminates the oldest Envoy process immediately, which can forcibly close its remaining connections. Space out consecutive updates by at least the drain period.
+ ELB for Envoy does not expose Envoy's admin interface. If you enable it in your bootstrap, see [Use the Envoy admin interface securely](envoy-admin-interface.md) for the supported access controls, HTTP paths, and methods.

For AWS WAF inspection limitations, see [Protect a proxy with AWS WAF](waf.md).

## Lua restrictions
<a name="envoy-limits-lua"></a>

ELB for Envoy runs the Lua code in your configuration with a restricted set of Lua standard libraries. The restrictions apply to the Lua HTTP filter (`envoy.filters.http.lua`), the Lua cluster specifier (`envoy.router.cluster_specifier_plugin.lua`), and the Lua string matcher (`envoy.string_matcher.lua`).

**Lua standard library restrictions**

| Library | Restriction |
| --- | --- |
| `io`, `debug`, `package`, `ffi`, `jit` | Not available. |
| Base functions | `load`, `loadstring`, `loadfile`, `dofile`, `require`, `module`, `getfenv`, `setfenv`, `newproxy`, and `collectgarbage` are not available. |
| `string` | `string.dump` is not available, and `getmetatable` on a string returns `false`. |
| `os` | Only `os.clock`, `os.date`, `os.difftime`, and `os.time` are available. |

The rest of the base, `string`, `table`, `math`, and `bit` libraries is available. Scripts must be Lua source text. Envoy rejects precompiled Lua bytecode.

## Unsupported features
<a name="envoy-limits-unsupported"></a>

ELB for Envoy does not support the following Envoy features:
+ Envoy dynamic modules (the `envoy.*.dynamic_modules` extensions).
+ The file, stderr, and stdout access loggers (`envoy.access_loggers.file`, `envoy.access_loggers.stderr`, and `envoy.access_loggers.stdout`) and the `admin.access_log_path` field. Envoy rejects a resource that uses any of them, including a resource delivered over xDS or loaded from a file in the configuration archive, and the update that carries that resource is not applied. To export access logs, use a network access logger: `envoy.access_loggers.open_telemetry`, `envoy.access_loggers.http_grpc`, `envoy.access_loggers.tcp_grpc`, or `envoy.access_loggers.fluentd`.
+ Network namespace fields. Envoy always creates sockets in the proxy's default network namespace. The `network_namespace_filepath` address field, the `filter_state_override` local address selector, and the `envoy.network.upstream_bind_override.network_namespace` filter-state key are not supported.
+ Envoy CLI flags. ELB for Envoy manages the Envoy command line, so you cannot set these flags. Control log levels through the `envoy.log_level` and `envoy.component_log_level` proxy attributes instead. For details, see [Troubleshoot ELB for Envoy](troubleshooting.md).
+ Non-V8 WebAssembly (Wasm) runtimes. ELB for Envoy supports only the V8 Wasm runtime (`envoy.wasm.runtime.v8`) for Wasm filters, access loggers, bootstrap extensions, and stat sinks. A Wasm configuration that leaves `vm_config.runtime` empty uses V8, and Envoy rejects one that names any other runtime.
