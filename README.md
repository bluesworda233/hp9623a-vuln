# HPE HP J9623A RPC Unauthorized Access Vulnerability

## Overview

A critical unauthorized RPC access vulnerability exists in the web management interface of the HPE HP J9623A Layer 3 Switch.

The vulnerability allows unauthenticated attackers to directly invoke privileged backend JSON/RPC functions without authentication or authorization.

An attacker may abuse this issue to:

- Leak administrator credentials
- Obtain configuration files
- Modify switch configuration
- Reboot the switch remotely
- Perform unauthorized management operations

---

## Vendor

- Vendor: Hewlett Packard Enterprise (HPE)
- Product: HP J9623A Layer 3 Switch

---

## Affected Versions

Confirmed affected versions:

```text
RA.15.08.0009
ROM RA.15.10
