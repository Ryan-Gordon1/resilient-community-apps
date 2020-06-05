# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_joe_sandbox_analysis"""

from __future__ import print_function
from resilient_circuits.util import *


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     artifact_id
    #     attachment_id
    #     incident_id
    #     jsb_report_type
    #   Message Destinations:
    #     joe_sandbox_message_destination
    #   Functions:
    #     fn_joe_sandbox_analysis
    #   Workflows:
    #     example_joe_sandbox_analysis_attachment
    #     example_joe_sandbox_artifact
    #   Rules:
    #     Example: Joe Sandbox Analysis [Artifact]
    #     Example: Joe Sandbox Analysis [Attachment]


    yield ImportDefinition(u"""
ewogICJ0YXNrX29yZGVyIjogW10sCiAgIndvcmtmbG93cyI6IFt7CiAgICAidXVpZCI6ICJiNjg4
OGE0Yi0xY2RmLTRiMWUtOTQxNC03MWViNGJiMTIzMmYiLAogICAgImRlc2NyaXB0aW9uIjogIkFu
IGV4YW1wbGUgb2YgaGF2aW5nIGFuIGF0dGFjaG1lbnQgc2FtcGxlIGFuYWx5emVkIGJ5IEpvZSBT
YW5kYm94IiwKICAgICJvYmplY3RfdHlwZSI6ICJhdHRhY2htZW50IiwKICAgICJleHBvcnRfa2V5
IjogImV4YW1wbGVfam9lX3NhbmRib3hfYW5hbHlzaXNfYXR0YWNobWVudCIsCiAgICAid29ya2Zs
b3dfaWQiOiAyLAogICAgImxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AcmVzLmNvbSIsCiAgICAi
Y29udGVudCI6IHsKICAgICAgInhtbCI6ICI8P3htbCB2ZXJzaW9uPVwiMS4wXCIgZW5jb2Rpbmc9
XCJVVEYtOFwiPz48ZGVmaW5pdGlvbnMgeG1sbnM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9C
UE1OLzIwMTAwNTI0L01PREVMXCIgeG1sbnM6YnBtbmRpPVwiaHR0cDovL3d3dy5vbWcub3JnL3Nw
ZWMvQlBNTi8yMDEwMDUyNC9ESVwiIHhtbG5zOm9tZ2RjPVwiaHR0cDovL3d3dy5vbWcub3JnL3Nw
ZWMvREQvMjAxMDA1MjQvRENcIiB4bWxuczpvbWdkaT1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVj
L0RELzIwMTAwNTI0L0RJXCIgeG1sbnM6cmVzaWxpZW50PVwiaHR0cDovL3Jlc2lsaWVudC5pYm0u
Y29tL2JwbW5cIiB4bWxuczp4c2Q9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYVwi
IHhtbG5zOnhzaT1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlXCIg
dGFyZ2V0TmFtZXNwYWNlPVwiaHR0cDovL3d3dy5jYW11bmRhLm9yZy90ZXN0XCI+PHByb2Nlc3Mg
aWQ9XCJleGFtcGxlX2pvZV9zYW5kYm94X2FuYWx5c2lzX2F0dGFjaG1lbnRcIiBpc0V4ZWN1dGFi
bGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1wbGU6IEpvZSBTYW5kYm94IEFuYWx5c2lzIFtBdHRhY2ht
ZW50XVwiPjxkb2N1bWVudGF0aW9uPkFuIGV4YW1wbGUgb2YgaGF2aW5nIGFuIGF0dGFjaG1lbnQg
c2FtcGxlIGFuYWx5emVkIGJ5IEpvZSBTYW5kYm94PC9kb2N1bWVudGF0aW9uPjxzdGFydEV2ZW50
IGlkPVwiU3RhcnRFdmVudF8xNTVhc3htXCI+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xMmljN2c0
PC9vdXRnb2luZz48L3N0YXJ0RXZlbnQ+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMDkyMGxwNVwi
PjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHprNGVsajwvaW5jb21pbmc+PC9lbmRFdmVudD48c2Vy
dmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18xMGhrbG4xXCIgbmFtZT1cIkpvZSBTYW5kYm94IEFu
YWx5c2lzXCIgcmVzaWxpZW50OnR5cGU9XCJmdW5jdGlvblwiPjxleHRlbnNpb25FbGVtZW50cz48
cmVzaWxpZW50OmZ1bmN0aW9uIHV1aWQ9XCI3NmQ2M2M4Ni1jNWZkLTQxZjctYTQzYS0yOTIyZDZm
YjNkOTFcIj57XCJpbnB1dHNcIjp7XCIyNGNkNjVmYS1lMDZjLTQ1ODAtOGE3Yi05MjM1ODVmOWQ4
MWJcIjp7XCJpbnB1dF90eXBlXCI6XCJzdGF0aWNcIixcInN0YXRpY19pbnB1dFwiOntcIm11bHRp
c2VsZWN0X3ZhbHVlXCI6W10sXCJzZWxlY3RfdmFsdWVcIjpcIjIyMmZhZjJiLWY0NDYtNDcxZS1h
M2M3LTllYjIxYzgwNzMxOFwifX19LFwicHJlX3Byb2Nlc3Npbmdfc2NyaXB0XCI6XCJpbnB1dHMu
aW5jaWRlbnRfaWQgPSBpbmNpZGVudC5pZFxcbmlucHV0cy5hdHRhY2htZW50X2lkID0gYXR0YWNo
bWVudC5pZFwiLFwicmVzdWx0X25hbWVcIjpcIlwiLFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwi
OlwiY29sb3IgPSBcXFwiIzQ1YmMyN1xcXCJcXG5cXG5pZiAocmVzdWx0cy5hbmFseXNpc19zdGF0
dXMgIT0gXFxcImNsZWFuXFxcIik6XFxuICBjb2xvciA9IFxcXCIjZmY0MDJiXFxcIlxcbiAgXFxu
bm90ZVRleHQgPSBcXFwiXFxcIlxcXCImbHQ7YnImZ3Q7Sm9lIFNhbmRib3ggYW5hbHlzaXMgJmx0
O2ImZ3Q7ezB9Jmx0Oy9iJmd0OyBjb21wbGV0ZVxcbiAgICAgICAgICAgICAgJmx0O2ImZ3Q7QXR0
YWNobWVudDombHQ7L2ImZ3Q7ICd7MX0nXFxuICAgICAgICAgICAgICAmbHQ7YiZndDtSZXBvcnQg
VVJMOiZsdDsvYiZndDsgJmx0O2EgaHJlZj0nezJ9JyZndDt7Mn0mbHQ7L2EmZ3Q7XFxuICAgICAg
ICAgICAgICAmbHQ7YiZndDtEZXRlY3Rpb24gU3RhdHVzOiZsdDsvYiZndDsgJmx0O2Igc3R5bGU9
XFxcImNvbG9yOiB7M31cXFwiJmd0O3s0fSZsdDsvYiZndDtcXFwiXFxcIlxcXCIuZm9ybWF0KHJl
c3VsdHMuYW5hbHlzaXNfcmVwb3J0X25hbWUsIGF0dGFjaG1lbnQubmFtZSwgcmVzdWx0cy5hbmFs
eXNpc19yZXBvcnRfdXJsLCBjb2xvciwgcmVzdWx0cy5hbmFseXNpc19zdGF0dXMpXFxuXFxuaW5j
aWRlbnQuYWRkTm90ZShoZWxwZXIuY3JlYXRlUmljaFRleHQobm90ZVRleHQpKVwifTwvcmVzaWxp
ZW50OmZ1bmN0aW9uPjwvZXh0ZW5zaW9uRWxlbWVudHM+PGluY29taW5nPlNlcXVlbmNlRmxvd18x
MmljN2c0PC9pbmNvbWluZz48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzB6azRlbGo8L291dGdvaW5n
Pjwvc2VydmljZVRhc2s+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18xMmljN2c0XCIg
c291cmNlUmVmPVwiU3RhcnRFdmVudF8xNTVhc3htXCIgdGFyZ2V0UmVmPVwiU2VydmljZVRhc2tf
MTBoa2xuMVwiLz48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzB6azRlbGpcIiBzb3Vy
Y2VSZWY9XCJTZXJ2aWNlVGFza18xMGhrbG4xXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMDkyMGxw
NVwiLz48dGV4dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCI+PHRleHQ+
U3RhcnQgeW91ciB3b3JrZmxvdyBoZXJlPC90ZXh0PjwvdGV4dEFubm90YXRpb24+PGFzc29jaWF0
aW9uIGlkPVwiQXNzb2NpYXRpb25fMXNldWo0OFwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1
YXN4bVwiIHRhcmdldFJlZj1cIlRleHRBbm5vdGF0aW9uXzFreHhpeXRcIi8+PC9wcm9jZXNzPjxi
cG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1ORGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUg
YnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBpZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1O
U2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRf
MTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1c
IjE2MlwiIHk9XCIxODhcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9
XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxNTdcIiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJl
bD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJUZXh0
QW5ub3RhdGlvbl8xa3h4aXl0XCIgaWQ9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0X2RpXCI+PG9t
Z2RjOkJvdW5kcyBoZWlnaHQ9XCIzMFwiIHdpZHRoPVwiMTAwXCIgeD1cIjk5XCIgeT1cIjI1NFwi
Lz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIkFzc29j
aWF0aW9uXzFzZXVqNDhcIiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhfZGlcIj48b21nZGk6d2F5
cG9pbnQgeD1cIjE2OVwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjIwXCIvPjxvbWdk
aTp3YXlwb2ludCB4PVwiMTUzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyNTRcIi8+
PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJFbmRFdmVu
dF8wOTIwbHA1XCIgaWQ9XCJFbmRFdmVudF8wOTIwbHA1X2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWln
aHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNTgzXCIgeT1cIjE4OFwiLz48YnBtbmRpOkJQTU5M
YWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjYwMVwiIHk9
XCIyMjdcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQ
TU5TaGFwZSBicG1uRWxlbWVudD1cIlNlcnZpY2VUYXNrXzEwaGtsbjFcIiBpZD1cIlNlcnZpY2VU
YXNrXzEwaGtsbjFfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjgwXCIgd2lkdGg9XCIxMDBc
IiB4PVwiMzM2XCIgeT1cIjE2NlwiLz48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5kaTpCUE1ORWRn
ZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18xMmljN2c0XCIgaWQ9XCJTZXF1ZW5jZUZsb3df
MTJpYzdnNF9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiMTk4XCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCIzMzZcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhl
aWdodD1cIjEzXCIgd2lkdGg9XCIwXCIgeD1cIjI2N1wiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBN
TkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJT
ZXF1ZW5jZUZsb3dfMHprNGVsalwiIGlkPVwiU2VxdWVuY2VGbG93XzB6azRlbGpfZGlcIj48b21n
ZGk6d2F5cG9pbnQgeD1cIjQzNlwiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIv
PjxvbWdkaTp3YXlwb2ludCB4PVwiNTgzXCIgeHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIy
MDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRo
PVwiMFwiIHg9XCI1MDkuNVwiIHk9XCIxODRcIi8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRp
OkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1ORGlhZ3JhbT48L2RlZmlu
aXRpb25zPiIsCiAgICAgICJ3b3JrZmxvd19pZCI6ICJleGFtcGxlX2pvZV9zYW5kYm94X2FuYWx5
c2lzX2F0dGFjaG1lbnQiLAogICAgICAidmVyc2lvbiI6IDIKICAgIH0sCiAgICAibGFzdF9tb2Rp
ZmllZF90aW1lIjogMTUzMTczNjM2NzIwOSwKICAgICJjcmVhdG9yX2lkIjogImFkbWluQHJlcy5j
b20iLAogICAgImFjdGlvbnMiOiBbXSwKICAgICJwcm9ncmFtbWF0aWNfbmFtZSI6ICJleGFtcGxl
X2pvZV9zYW5kYm94X2FuYWx5c2lzX2F0dGFjaG1lbnQiLAogICAgIm5hbWUiOiAiRXhhbXBsZTog
Sm9lIFNhbmRib3ggQW5hbHlzaXMgW0F0dGFjaG1lbnRdIgogIH0sIHsKICAgICJ1dWlkIjogImFi
NmFhYTYxLTBmNzAtNDQzMi1iMTVmLWI5OTRiNDZiMzBmNSIsCiAgICAiZGVzY3JpcHRpb24iOiAi
QW4gZXhhbXBsZSBvZiBoYXZpbmcgYW4gYXJ0aWZhY3Qgc2FtcGxlIGFuYWx5emVkIGJ5IEpvZSBT
YW5kYm94IiwKICAgICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsCiAgICAiZXhwb3J0X2tleSI6
ICJleGFtcGxlX2pvZV9zYW5kYm94X2FydGlmYWN0IiwKICAgICJ3b3JrZmxvd19pZCI6IDMsCiAg
ICAibGFzdF9tb2RpZmllZF9ieSI6ICJhZG1pbkByZXMuY29tIiwKICAgICJjb250ZW50Ijogewog
ICAgICAieG1sIjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI/Pjxk
ZWZpbml0aW9ucyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQv
TU9ERUxcIiB4bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAw
NTI0L0RJXCIgeG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUy
NC9EQ1wiIHhtbG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQv
RElcIiB4bWxuczpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5jb20vYnBtblwiIHht
bG5zOnhzZD1cImh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hXCIgeG1sbnM6eHNpPVwi
aHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0YXJnZXROYW1lc3Bh
Y2U9XCJodHRwOi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBpZD1cImV4YW1wbGVf
am9lX3NhbmRib3hfYXJ0aWZhY3RcIiBpc0V4ZWN1dGFibGU9XCJ0cnVlXCIgbmFtZT1cIkV4YW1w
bGU6IEpvZSBTYW5kYm94IFtBcnRpZmFjdF1cIj48ZG9jdW1lbnRhdGlvbj5BbiBleGFtcGxlIG9m
IGhhdmluZyBhbiBhcnRpZmFjdCBzYW1wbGUgYW5hbHl6ZWQgYnkgSm9lIFNhbmRib3g8L2RvY3Vt
ZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFydEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+
U2VxdWVuY2VGbG93XzBuZ3VkOXk8L291dGdvaW5nPjwvc3RhcnRFdmVudD48ZW5kRXZlbnQgaWQ9
XCJFbmRFdmVudF8xNmZydGxvXCI+PGluY29taW5nPlNlcXVlbmNlRmxvd18xdjN5ZTkxPC9pbmNv
bWluZz48L2VuZEV2ZW50PjxzZXJ2aWNlVGFzayBpZD1cIlNlcnZpY2VUYXNrXzBnd2JveWhcIiBu
YW1lPVwiSm9lIFNhbmRib3ggQW5hbHlzaXNcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+
PGV4dGVuc2lvbkVsZW1lbnRzPjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjc2ZDYzYzg2LWM1
ZmQtNDFmNy1hNDNhLTI5MjJkNmZiM2Q5MVwiPntcImlucHV0c1wiOntcIjI0Y2Q2NWZhLWUwNmMt
NDU4MC04YTdiLTkyMzU4NWY5ZDgxYlwiOntcImlucHV0X3R5cGVcIjpcInN0YXRpY1wiLFwic3Rh
dGljX2lucHV0XCI6e1wibXVsdGlzZWxlY3RfdmFsdWVcIjpbXSxcInNlbGVjdF92YWx1ZVwiOlwi
MjIyZmFmMmItZjQ0Ni00NzFlLWEzYzctOWViMjFjODA3MzE4XCJ9fX0sXCJwcmVfcHJvY2Vzc2lu
Z19zY3JpcHRcIjpcImlucHV0cy5pbmNpZGVudF9pZCA9IGluY2lkZW50LmlkXFxuaW5wdXRzLmFy
dGlmYWN0X2lkID0gYXJ0aWZhY3QuaWRcIixcInJlc3VsdF9uYW1lXCI6XCJcIixcInBvc3RfcHJv
Y2Vzc2luZ19zY3JpcHRcIjpcImNvbG9yID0gXFxcIiM0NWJjMjdcXFwiXFxuXFxuaWYgKHJlc3Vs
dHMuYW5hbHlzaXNfc3RhdHVzICE9IFxcXCJjbGVhblxcXCIpOlxcbiAgY29sb3IgPSBcXFwiI2Zm
NDAyYlxcXCJcXG4gIFxcbm5vdGVUZXh0ID0gXFxcIlxcXCJcXFwiJmx0O2JyJmd0O0pvZSBTYW5k
Ym94IGFuYWx5c2lzICZsdDtiJmd0O3swfSZsdDsvYiZndDsgY29tcGxldGVcXG4gICAgICAgICAg
ICAgICZsdDtiJmd0O0FydGlmYWN0OiZsdDsvYiZndDsgJ3sxfSdcXG4gICAgICAgICAgICAgICZs
dDtiJmd0O1JlcG9ydCBVUkw6Jmx0Oy9iJmd0OyAmbHQ7YSBocmVmPSd7Mn0nJmd0O3syfSZsdDsv
YSZndDtcXG4gICAgICAgICAgICAgICZsdDtiJmd0O0RldGVjdGlvbiBTdGF0dXM6Jmx0Oy9iJmd0
OyAmbHQ7YiBzdHlsZT1cXFwiY29sb3I6IHszfVxcXCImZ3Q7ezR9Jmx0Oy9iJmd0O1xcXCJcXFwi
XFxcIi5mb3JtYXQocmVzdWx0cy5hbmFseXNpc19yZXBvcnRfbmFtZSwgYXJ0aWZhY3QudmFsdWUs
IHJlc3VsdHMuYW5hbHlzaXNfcmVwb3J0X3VybCwgY29sb3IsIHJlc3VsdHMuYW5hbHlzaXNfc3Rh
dHVzKVxcblxcbmluY2lkZW50LmFkZE5vdGUoaGVscGVyLmNyZWF0ZVJpY2hUZXh0KG5vdGVUZXh0
KSlcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNvbWluZz5T
ZXF1ZW5jZUZsb3dfMG5ndWQ5eTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxvd18xdjN5
ZTkxPC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1ZW5jZUZs
b3dfMG5ndWQ5eVwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdldFJlZj1c
IlNlcnZpY2VUYXNrXzBnd2JveWhcIi8+PHNlcXVlbmNlRmxvdyBpZD1cIlNlcXVlbmNlRmxvd18x
djN5ZTkxXCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMGd3Ym95aFwiIHRhcmdldFJlZj1cIkVu
ZEV2ZW50XzE2ZnJ0bG9cIi8+PHRleHRBbm5vdGF0aW9uIGlkPVwiVGV4dEFubm90YXRpb25fMWt4
eGl5dFwiPjx0ZXh0PlN0YXJ0IHlvdXIgd29ya2Zsb3cgaGVyZTwvdGV4dD48L3RleHRBbm5vdGF0
aW9uPjxhc3NvY2lhdGlvbiBpZD1cIkFzc29jaWF0aW9uXzFzZXVqNDhcIiBzb3VyY2VSZWY9XCJT
dGFydEV2ZW50XzE1NWFzeG1cIiB0YXJnZXRSZWY9XCJUZXh0QW5ub3RhdGlvbl8xa3h4aXl0XCIv
PjwvcHJvY2Vzcz48YnBtbmRpOkJQTU5EaWFncmFtIGlkPVwiQlBNTkRpYWdyYW1fMVwiPjxicG1u
ZGk6QlBNTlBsYW5lIGJwbW5FbGVtZW50PVwidW5kZWZpbmVkXCIgaWQ9XCJCUE1OUGxhbmVfMVwi
PjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVtZW50PVwiU3RhcnRFdmVudF8xNTVhc3htXCIgaWQ9
XCJTdGFydEV2ZW50XzE1NWFzeG1fZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjM2XCIgd2lk
dGg9XCIzNlwiIHg9XCIxNjJcIiB5PVwiMTg4XCIvPjxicG1uZGk6QlBNTkxhYmVsPjxvbWdkYzpC
b3VuZHMgaGVpZ2h0PVwiMFwiIHdpZHRoPVwiOTBcIiB4PVwiMTU3XCIgeT1cIjIyM1wiLz48L2Jw
bW5kaTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5F
bGVtZW50PVwiVGV4dEFubm90YXRpb25fMWt4eGl5dFwiIGlkPVwiVGV4dEFubm90YXRpb25fMWt4
eGl5dF9kaVwiPjxvbWdkYzpCb3VuZHMgaGVpZ2h0PVwiMzBcIiB3aWR0aD1cIjEwMFwiIHg9XCI5
OVwiIHk9XCIyNTRcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBNTkVkZ2UgYnBtbkVs
ZW1lbnQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4XCIgaWQ9XCJBc3NvY2lhdGlvbl8xc2V1ajQ4X2Rp
XCI+PG9tZ2RpOndheXBvaW50IHg9XCIxNjlcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1c
IjIyMFwiLz48b21nZGk6d2F5cG9pbnQgeD1cIjE1M1wiIHhzaTp0eXBlPVwib21nZGM6UG9pbnRc
IiB5PVwiMjU0XCIvPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTlNoYXBlIGJwbW5FbGVt
ZW50PVwiRW5kRXZlbnRfMTZmcnRsb1wiIGlkPVwiRW5kRXZlbnRfMTZmcnRsb19kaVwiPjxvbWdk
YzpCb3VuZHMgaGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjYzNFwiIHk9XCIxODhcIi8+
PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwi
IHg9XCI2NTJcIiB5PVwiMjI3XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hh
cGU+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18wZ3dib3loXCIg
aWQ9XCJTZXJ2aWNlVGFza18wZ3dib3loX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwi
IHdpZHRoPVwiMTAwXCIgeD1cIjM1MlwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxi
cG1uZGk6QlBNTkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMG5ndWQ5eVwiIGlkPVwi
U2VxdWVuY2VGbG93XzBuZ3VkOXlfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjE5OFwiIHhzaTp0
eXBlPVwib21nZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzUyXCIg
eHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9t
Z2RjOkJvdW5kcyBoZWlnaHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCIyNzVcIiB5PVwiMTg0LjVc
Ii8+PC9icG1uZGk6QlBNTkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjxicG1uZGk6QlBNTkVkZ2Ug
YnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMXYzeWU5MVwiIGlkPVwiU2VxdWVuY2VGbG93XzF2
M3llOTFfZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjQ1MlwiIHhzaTp0eXBlPVwib21nZGM6UG9p
bnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiNjM0XCIgeHNpOnR5cGU9XCJvbWdk
YzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWln
aHQ9XCIxM1wiIHdpZHRoPVwiMFwiIHg9XCI1NDNcIiB5PVwiMTg0LjVcIi8+PC9icG1uZGk6QlBN
TkxhYmVsPjwvYnBtbmRpOkJQTU5FZGdlPjwvYnBtbmRpOkJQTU5QbGFuZT48L2JwbW5kaTpCUE1O
RGlhZ3JhbT48L2RlZmluaXRpb25zPiIsCiAgICAgICJ3b3JrZmxvd19pZCI6ICJleGFtcGxlX2pv
ZV9zYW5kYm94X2FydGlmYWN0IiwKICAgICAgInZlcnNpb24iOiAyCiAgICB9LAogICAgImxhc3Rf
bW9kaWZpZWRfdGltZSI6IDE1MzE3MzYzNDk0MzAsCiAgICAiY3JlYXRvcl9pZCI6ICJhZG1pbkBy
ZXMuY29tIiwKICAgICJhY3Rpb25zIjogW10sCiAgICAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhh
bXBsZV9qb2Vfc2FuZGJveF9hcnRpZmFjdCIsCiAgICAibmFtZSI6ICJFeGFtcGxlOiBKb2UgU2Fu
ZGJveCBbQXJ0aWZhY3RdIgogIH1dLAogICJhY3Rpb25zIjogW3sKICAgICJsb2dpY190eXBlIjog
ImFueSIsCiAgICAibmFtZSI6ICJFeGFtcGxlOiBKb2UgU2FuZGJveCBBbmFseXNpcyBbQXJ0aWZh
Y3RdIiwKICAgICJ2aWV3X2l0ZW1zIjogW10sCiAgICAidHlwZSI6IDEsCiAgICAid29ya2Zsb3dz
IjogWyJleGFtcGxlX2pvZV9zYW5kYm94X2FydGlmYWN0Il0sCiAgICAib2JqZWN0X3R5cGUiOiAi
YXJ0aWZhY3QiLAogICAgInRpbWVvdXRfc2Vjb25kcyI6IDg2NDAwLAogICAgInV1aWQiOiAiMDUw
YzdjNzgtNWY0ZC00NmY2LWEyN2EtYWY4YTA3ZTdiNTE4IiwKICAgICJhdXRvbWF0aW9ucyI6IFtd
LAogICAgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogSm9lIFNhbmRib3ggQW5hbHlzaXMgW0FydGlm
YWN0XSIsCiAgICAiY29uZGl0aW9ucyI6IFt7CiAgICAgICJ0eXBlIjogbnVsbCwKICAgICAgImV2
YWx1YXRpb25faWQiOiBudWxsLAogICAgICAiZmllbGRfbmFtZSI6ICJhcnRpZmFjdC50eXBlIiwK
ICAgICAgIm1ldGhvZCI6ICJlcXVhbHMiLAogICAgICAidmFsdWUiOiAiT3RoZXIgRmlsZSIKICAg
IH0sIHsKICAgICAgInR5cGUiOiBudWxsLAogICAgICAiZXZhbHVhdGlvbl9pZCI6IG51bGwsCiAg
ICAgICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5cGUiLAogICAgICAibWV0aG9kIjogImVxdWFs
cyIsCiAgICAgICJ2YWx1ZSI6ICJETlMgTmFtZSIKICAgIH0sIHsKICAgICAgInR5cGUiOiBudWxs
LAogICAgICAiZXZhbHVhdGlvbl9pZCI6IG51bGwsCiAgICAgICJmaWVsZF9uYW1lIjogImFydGlm
YWN0LnR5cGUiLAogICAgICAibWV0aG9kIjogImVxdWFscyIsCiAgICAgICJ2YWx1ZSI6ICJVUkwi
CiAgICB9LCB7CiAgICAgICJ0eXBlIjogbnVsbCwKICAgICAgImV2YWx1YXRpb25faWQiOiBudWxs
LAogICAgICAiZmllbGRfbmFtZSI6ICJhcnRpZmFjdC50eXBlIiwKICAgICAgIm1ldGhvZCI6ICJl
cXVhbHMiLAogICAgICAidmFsdWUiOiAiRW1haWwgQXR0YWNobWVudCIKICAgIH0sIHsKICAgICAg
InR5cGUiOiBudWxsLAogICAgICAiZXZhbHVhdGlvbl9pZCI6IG51bGwsCiAgICAgICJmaWVsZF9u
YW1lIjogImFydGlmYWN0LnR5cGUiLAogICAgICAibWV0aG9kIjogImVxdWFscyIsCiAgICAgICJ2
YWx1ZSI6ICJVUkkgUGF0aCIKICAgIH0sIHsKICAgICAgInR5cGUiOiBudWxsLAogICAgICAiZXZh
bHVhdGlvbl9pZCI6IG51bGwsCiAgICAgICJmaWVsZF9uYW1lIjogImFydGlmYWN0LnR5cGUiLAog
ICAgICAibWV0aG9kIjogImVxdWFscyIsCiAgICAgICJ2YWx1ZSI6ICJJUCBBZGRyZXNzIgogICAg
fV0sCiAgICAiaWQiOiAyOCwKICAgICJtZXNzYWdlX2Rlc3RpbmF0aW9ucyI6IFtdCiAgfSwgewog
ICAgImxvZ2ljX3R5cGUiOiAiYWxsIiwKICAgICJuYW1lIjogIkV4YW1wbGU6IEpvZSBTYW5kYm94
IEFuYWx5c2lzIFtBdHRhY2htZW50XSIsCiAgICAidmlld19pdGVtcyI6IFtdLAogICAgInR5cGUi
OiAxLAogICAgIndvcmtmbG93cyI6IFsiZXhhbXBsZV9qb2Vfc2FuZGJveF9hbmFseXNpc19hdHRh
Y2htZW50Il0sCiAgICAib2JqZWN0X3R5cGUiOiAiYXR0YWNobWVudCIsCiAgICAidGltZW91dF9z
ZWNvbmRzIjogODY0MDAsCiAgICAidXVpZCI6ICIzZGYzMTJiMy1mZDQ1LTQ2ZGItOWEyYy01ZWFl
MzdkNjk4Y2EiLAogICAgImF1dG9tYXRpb25zIjogW10sCiAgICAiZXhwb3J0X2tleSI6ICJFeGFt
cGxlOiBKb2UgU2FuZGJveCBBbmFseXNpcyBbQXR0YWNobWVudF0iLAogICAgImNvbmRpdGlvbnMi
OiBbXSwKICAgICJpZCI6IDI5LAogICAgIm1lc3NhZ2VfZGVzdGluYXRpb25zIjogW10KICB9XSwK
ICAibGF5b3V0cyI6IFtdLAogICJleHBvcnRfZm9ybWF0X3ZlcnNpb24iOiAyLAogICJpZCI6IDMs
CiAgImluZHVzdHJpZXMiOiBudWxsLAogICJwaGFzZXMiOiBbXSwKICAiYWN0aW9uX29yZGVyIjog
W10sCiAgImdlb3MiOiBudWxsLAogICJzZXJ2ZXJfdmVyc2lvbiI6IHsKICAgICJtYWpvciI6IDMw
LAogICAgInZlcnNpb24iOiAiMzAuMC4wIiwKICAgICJidWlsZF9udW1iZXIiOiAwLAogICAgIm1p
bm9yIjogMAogIH0sCiAgInRpbWVmcmFtZXMiOiBudWxsLAogICJ3b3Jrc3BhY2VzIjogW10sCiAg
ImF1dG9tYXRpY190YXNrcyI6IFtdLAogICJmdW5jdGlvbnMiOiBbewogICAgImRpc3BsYXlfbmFt
ZSI6ICJKb2UgU2FuZGJveCBBbmFseXNpcyIsCiAgICAiZGVzY3JpcHRpb24iOiB7CiAgICAgICJj
b250ZW50IjogIkEgZnVuY3Rpb24gdGhhdCBhbGxvd3MgYW4gQXR0YWNobWVudCBvciBBcnRpZmFj
dCAoRmlsZS9VUkwpIHRvIGJlIGFuYWx5emVkIGJ5IEpvZSBTYW5kYm94IiwKICAgICAgImZvcm1h
dCI6ICJ0ZXh0IgogICAgfSwKICAgICJjcmVhdG9yIjogewogICAgICAiZGlzcGxheV9uYW1lIjog
IlNoYW5lIEN1cnRpbiIsCiAgICAgICJ0eXBlIjogInVzZXIiLAogICAgICAiaWQiOiAxLAogICAg
ICAibmFtZSI6ICJhZG1pbkByZXMuY29tIgogICAgfSwKICAgICJ2aWV3X2l0ZW1zIjogW3sKICAg
ICAgInNob3dfaWYiOiBudWxsLAogICAgICAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwKICAg
ICAgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwKICAgICAgImVsZW1lbnQiOiAiZmllbGRfdXVp
ZCIsCiAgICAgICJjb250ZW50IjogImVhZDIxNGMyLTEzZmUtNDNmNi1hM2M3LTY3NmE4ODMzOGRi
YiIsCiAgICAgICJzdGVwX2xhYmVsIjogbnVsbAogICAgfSwgewogICAgICAic2hvd19pZiI6IG51
bGwsCiAgICAgICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLAogICAgICAic2hvd19saW5rX2hl
YWRlciI6IGZhbHNlLAogICAgICAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwKICAgICAgImNvbnRl
bnQiOiAiMTdjM2U2NTItNjU1OS00OTM1LTlmOTUtNzQzNzRjYTM3YTdiIiwKICAgICAgInN0ZXBf
bGFiZWwiOiBudWxsCiAgICB9LCB7CiAgICAgICJzaG93X2lmIjogbnVsbCwKICAgICAgImZpZWxk
X3R5cGUiOiAiX19mdW5jdGlvbiIsCiAgICAgICJzaG93X2xpbmtfaGVhZGVyIjogZmFsc2UsCiAg
ICAgICJlbGVtZW50IjogImZpZWxkX3V1aWQiLAogICAgICAiY29udGVudCI6ICJlZmRiY2E3ZS02
YWU4LTQyNjktYTNkMS04MGYxNzE2YTYyMjIiLAogICAgICAic3RlcF9sYWJlbCI6IG51bGwKICAg
IH0sIHsKICAgICAgInNob3dfaWYiOiBudWxsLAogICAgICAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0
aW9uIiwKICAgICAgInNob3dfbGlua19oZWFkZXIiOiBmYWxzZSwKICAgICAgImVsZW1lbnQiOiAi
ZmllbGRfdXVpZCIsCiAgICAgICJjb250ZW50IjogIjI0Y2Q2NWZhLWUwNmMtNDU4MC04YTdiLTky
MzU4NWY5ZDgxYiIsCiAgICAgICJzdGVwX2xhYmVsIjogbnVsbAogICAgfV0sCiAgICAiZXhwb3J0
X2tleSI6ICJmbl9qb2Vfc2FuZGJveF9hbmFseXNpcyIsCiAgICAidXVpZCI6ICI3NmQ2M2M4Ni1j
NWZkLTQxZjctYTQzYS0yOTIyZDZmYjNkOTEiLAogICAgImxhc3RfbW9kaWZpZWRfYnkiOiB7CiAg
ICAgICJkaXNwbGF5X25hbWUiOiAiU2hhbmUgQ3VydGluIiwKICAgICAgInR5cGUiOiAidXNlciIs
CiAgICAgICJpZCI6IDEsCiAgICAgICJuYW1lIjogImFkbWluQHJlcy5jb20iCiAgICB9LAogICAg
InZlcnNpb24iOiAyLAogICAgIndvcmtmbG93cyI6IFt7CiAgICAgICJkZXNjcmlwdGlvbiI6IG51
bGwsCiAgICAgICJvYmplY3RfdHlwZSI6ICJhcnRpZmFjdCIsCiAgICAgICJhY3Rpb25zIjogW10s
CiAgICAgICJuYW1lIjogIkV4YW1wbGU6IEpvZSBTYW5kYm94IFtBcnRpZmFjdF0iLAogICAgICAi
d29ya2Zsb3dfaWQiOiAzLAogICAgICAicHJvZ3JhbW1hdGljX25hbWUiOiAiZXhhbXBsZV9qb2Vf
c2FuZGJveF9hcnRpZmFjdCIsCiAgICAgICJ1dWlkIjogbnVsbAogICAgfSwgewogICAgICAiZGVz
Y3JpcHRpb24iOiBudWxsLAogICAgICAib2JqZWN0X3R5cGUiOiAiYXR0YWNobWVudCIsCiAgICAg
ICJhY3Rpb25zIjogW10sCiAgICAgICJuYW1lIjogIkV4YW1wbGU6IEpvZSBTYW5kYm94IEFuYWx5
c2lzIFtBdHRhY2htZW50XSIsCiAgICAgICJ3b3JrZmxvd19pZCI6IDIsCiAgICAgICJwcm9ncmFt
bWF0aWNfbmFtZSI6ICJleGFtcGxlX2pvZV9zYW5kYm94X2FuYWx5c2lzX2F0dGFjaG1lbnQiLAog
ICAgICAidXVpZCI6IG51bGwKICAgIH1dLAogICAgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1MzE3
MzYzMzI5MDIsCiAgICAiZGVzdGluYXRpb25faGFuZGxlIjogImpvZV9zYW5kYm94X21lc3NhZ2Vf
ZGVzdGluYXRpb24iLAogICAgImlkIjogMiwKICAgICJuYW1lIjogImZuX2pvZV9zYW5kYm94X2Fu
YWx5c2lzIgogIH1dLAogICJub3RpZmljYXRpb25zIjogbnVsbCwKICAicmVndWxhdG9ycyI6IG51
bGwsCiAgImluY2lkZW50X3R5cGVzIjogW3sKICAgICJjcmVhdGVfZGF0ZSI6IDE1MzE3Mzg3NTcw
MDUsCiAgICAiZGVzY3JpcHRpb24iOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwp
IiwKICAgICJleHBvcnRfa2V5IjogIkN1c3RvbWl6YXRpb24gUGFja2FnZXMgKGludGVybmFsKSIs
CiAgICAiaWQiOiAwLAogICAgIm5hbWUiOiAiQ3VzdG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJu
YWwpIiwKICAgICJ1cGRhdGVfZGF0ZSI6IDE1MzE3Mzg3NTcwMDUsCiAgICAidXVpZCI6ICJiZmVl
YzJkNC0zNzcwLTExZTgtYWQzOS00YTAwMDQwNDRhYTAiLAogICAgImVuYWJsZWQiOiBmYWxzZSwK
ICAgICJzeXN0ZW0iOiBmYWxzZSwKICAgICJwYXJlbnRfaWQiOiBudWxsLAogICAgImhpZGRlbiI6
IGZhbHNlCiAgfV0sCiAgInNjcmlwdHMiOiBbXSwKICAidHlwZXMiOiBbXSwKICAibWVzc2FnZV9k
ZXN0aW5hdGlvbnMiOiBbewogICAgInV1aWQiOiAiZGQ3ODlkYjgtMmEwNS00OGI5LTllOTAtNzVi
NDlhMTBlZWVkIiwKICAgICJleHBvcnRfa2V5IjogImpvZV9zYW5kYm94X21lc3NhZ2VfZGVzdGlu
YXRpb24iLAogICAgIm5hbWUiOiAiSm9lIFNhbmRib3ggTWVzc2FnZSBEZXN0aW5hdGlvbiIsCiAg
ICAiZGVzdGluYXRpb25fdHlwZSI6IDAsCiAgICAicHJvZ3JhbW1hdGljX25hbWUiOiAiam9lX3Nh
bmRib3hfbWVzc2FnZV9kZXN0aW5hdGlvbiIsCiAgICAiZXhwZWN0X2FjayI6IHRydWUsCiAgICAi
dXNlcnMiOiBbImFkbWluQHJlcy5jb20iXQogIH1dLAogICJpbmNpZGVudF9hcnRpZmFjdF90eXBl
cyI6IFtdLAogICJyb2xlcyI6IFtdLAogICJmaWVsZHMiOiBbewogICAgIm9wZXJhdGlvbnMiOiBb
XSwKICAgICJyZWFkX29ubHkiOiB0cnVlLAogICAgIm5hbWUiOiAiaW5jX3RyYWluaW5nIiwKICAg
ICJ0ZW1wbGF0ZXMiOiBbXSwKICAgICJ0eXBlX2lkIjogMCwKICAgICJjaG9zZW4iOiBmYWxzZSwK
ICAgICJ0ZXh0IjogIlNpbXVsYXRpb24iLAogICAgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6
IGZhbHNlLAogICAgImV4cG9ydF9rZXkiOiAiaW5jaWRlbnQvaW5jX3RyYWluaW5nIiwKICAgICJ0
b29sdGlwIjogIldoZXRoZXIgdGhlIGluY2lkZW50IGlzIGEgc2ltdWxhdGlvbiBvciBhIHJlZ3Vs
YXIgaW5jaWRlbnQuICBUaGlzIGZpZWxkIGlzIHJlYWQtb25seS4iLAogICAgInJpY2hfdGV4dCI6
IGZhbHNlLAogICAgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LAogICAgInByZWZpeCI6IG51bGwsCiAg
ICAiaW50ZXJuYWwiOiBmYWxzZSwKICAgICJ2YWx1ZXMiOiBbXSwKICAgICJibGFua19vcHRpb24i
OiBmYWxzZSwKICAgICJpbnB1dF90eXBlIjogImJvb2xlYW4iLAogICAgImNoYW5nZWFibGUiOiB0
cnVlLAogICAgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsCiAgICAiaWQiOiAxMTUsCiAgICAi
dXVpZCI6ICJjM2YwZTNlZC0yMWUxLTRkNTMtYWZmYi1mZTVjYTMzMDhjY2EiCiAgfSwgewogICAg
Im9wZXJhdGlvbnMiOiBbXSwKICAgICJ0eXBlX2lkIjogMTEsCiAgICAib3BlcmF0aW9uX3Blcm1z
Ijoge30sCiAgICAidGV4dCI6ICJhcnRpZmFjdF9pZCIsCiAgICAiYmxhbmtfb3B0aW9uIjogZmFs
c2UsCiAgICAicHJlZml4IjogbnVsbCwKICAgICJjaGFuZ2VhYmxlIjogdHJ1ZSwKICAgICJpZCI6
IDE4NiwKICAgICJyZWFkX29ubHkiOiBmYWxzZSwKICAgICJ1dWlkIjogImVmZGJjYTdlLTZhZTgt
NDI2OS1hM2QxLTgwZjE3MTZhNjIyMiIsCiAgICAiY2hvc2VuIjogZmFsc2UsCiAgICAiaW5wdXRf
dHlwZSI6ICJudW1iZXIiLAogICAgInRvb2x0aXAiOiAiIiwKICAgICJpbnRlcm5hbCI6IGZhbHNl
LAogICAgInJpY2hfdGV4dCI6IGZhbHNlLAogICAgInRlbXBsYXRlcyI6IFtdLAogICAgImV4cG9y
dF9rZXkiOiAiX19mdW5jdGlvbi9hcnRpZmFjdF9pZCIsCiAgICAiaGlkZV9ub3RpZmljYXRpb24i
OiBmYWxzZSwKICAgICJwbGFjZWhvbGRlciI6ICIiLAogICAgIm5hbWUiOiAiYXJ0aWZhY3RfaWQi
LAogICAgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLAogICAgInZhbHVlcyI6IFtd
CiAgfSwgewogICAgIm9wZXJhdGlvbnMiOiBbXSwKICAgICJ0eXBlX2lkIjogMTEsCiAgICAib3Bl
cmF0aW9uX3Blcm1zIjoge30sCiAgICAidGV4dCI6ICJhdHRhY2htZW50X2lkIiwKICAgICJibGFu
a19vcHRpb24iOiBmYWxzZSwKICAgICJwcmVmaXgiOiBudWxsLAogICAgImNoYW5nZWFibGUiOiB0
cnVlLAogICAgImlkIjogMTg1LAogICAgInJlYWRfb25seSI6IGZhbHNlLAogICAgInV1aWQiOiAi
MTdjM2U2NTItNjU1OS00OTM1LTlmOTUtNzQzNzRjYTM3YTdiIiwKICAgICJjaG9zZW4iOiBmYWxz
ZSwKICAgICJpbnB1dF90eXBlIjogIm51bWJlciIsCiAgICAidG9vbHRpcCI6ICIiLAogICAgImlu
dGVybmFsIjogZmFsc2UsCiAgICAicmljaF90ZXh0IjogZmFsc2UsCiAgICAidGVtcGxhdGVzIjog
W10sCiAgICAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2F0dGFjaG1lbnRfaWQiLAogICAgImhp
ZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsCiAgICAicGxhY2Vob2xkZXIiOiAiIiwKICAgICJuYW1l
IjogImF0dGFjaG1lbnRfaWQiLAogICAgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNl
LAogICAgInZhbHVlcyI6IFtdCiAgfSwgewogICAgIm9wZXJhdGlvbnMiOiBbXSwKICAgICJ0eXBl
X2lkIjogMTEsCiAgICAib3BlcmF0aW9uX3Blcm1zIjoge30sCiAgICAidGV4dCI6ICJpbmNpZGVu
dF9pZCIsCiAgICAiYmxhbmtfb3B0aW9uIjogZmFsc2UsCiAgICAicHJlZml4IjogbnVsbCwKICAg
ICJjaGFuZ2VhYmxlIjogdHJ1ZSwKICAgICJpZCI6IDE4NCwKICAgICJyZWFkX29ubHkiOiBmYWxz
ZSwKICAgICJ1dWlkIjogImVhZDIxNGMyLTEzZmUtNDNmNi1hM2M3LTY3NmE4ODMzOGRiYiIsCiAg
ICAiY2hvc2VuIjogZmFsc2UsCiAgICAiaW5wdXRfdHlwZSI6ICJudW1iZXIiLAogICAgInRvb2x0
aXAiOiAiIiwKICAgICJpbnRlcm5hbCI6IGZhbHNlLAogICAgInJpY2hfdGV4dCI6IGZhbHNlLAog
ICAgInRlbXBsYXRlcyI6IFtdLAogICAgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9pbmNpZGVu
dF9pZCIsCiAgICAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwKICAgICJwbGFjZWhvbGRlciI6
ICIiLAogICAgIm5hbWUiOiAiaW5jaWRlbnRfaWQiLAogICAgImRlZmF1bHRfY2hvc2VuX2J5X3Nl
cnZlciI6IGZhbHNlLAogICAgInJlcXVpcmVkIjogImFsd2F5cyIsCiAgICAidmFsdWVzIjogW10K
ICB9LCB7CiAgICAib3BlcmF0aW9ucyI6IFtdLAogICAgInR5cGVfaWQiOiAxMSwKICAgICJvcGVy
YXRpb25fcGVybXMiOiB7fSwKICAgICJ0ZXh0IjogImpzYl9yZXBvcnRfdHlwZSIsCiAgICAiYmxh
bmtfb3B0aW9uIjogZmFsc2UsCiAgICAicHJlZml4IjogbnVsbCwKICAgICJjaGFuZ2VhYmxlIjog
dHJ1ZSwKICAgICJpZCI6IDE4MiwKICAgICJyZWFkX29ubHkiOiBmYWxzZSwKICAgICJ1dWlkIjog
IjI0Y2Q2NWZhLWUwNmMtNDU4MC04YTdiLTkyMzU4NWY5ZDgxYiIsCiAgICAiY2hvc2VuIjogZmFs
c2UsCiAgICAiaW5wdXRfdHlwZSI6ICJzZWxlY3QiLAogICAgInRvb2x0aXAiOiAiVGhlIGZvcm1h
dCBvZiB0aGUgcmVwb3J0IHRvIGJlIHJldHVybmVkIGZyb20gSm9lIFNhbmRib3giLAogICAgImlu
dGVybmFsIjogZmFsc2UsCiAgICAicmljaF90ZXh0IjogZmFsc2UsCiAgICAidGVtcGxhdGVzIjog
W10sCiAgICAiZXhwb3J0X2tleSI6ICJfX2Z1bmN0aW9uL2pzYl9yZXBvcnRfdHlwZSIsCiAgICAi
aGlkZV9ub3RpZmljYXRpb24iOiBmYWxzZSwKICAgICJwbGFjZWhvbGRlciI6ICIiLAogICAgIm5h
bWUiOiAianNiX3JlcG9ydF90eXBlIiwKICAgICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBm
YWxzZSwKICAgICJyZXF1aXJlZCI6ICJhbHdheXMiLAogICAgInZhbHVlcyI6IFt7CiAgICAgICJ1
dWlkIjogIjIyMmZhZjJiLWY0NDYtNDcxZS1hM2M3LTllYjIxYzgwNzMxOCIsCiAgICAgICJkZWZh
dWx0IjogdHJ1ZSwKICAgICAgImVuYWJsZWQiOiB0cnVlLAogICAgICAidmFsdWUiOiAyMDAsCiAg
ICAgICJsYWJlbCI6ICJodG1sIiwKICAgICAgImhpZGRlbiI6IGZhbHNlLAogICAgICAicHJvcGVy
dGllcyI6IG51bGwKICAgIH0sIHsKICAgICAgInV1aWQiOiAiZDc0NmFiMTktNzYxNS00NTgxLTg3
NDktZWNjYTI2NmIxYTU1IiwKICAgICAgImRlZmF1bHQiOiBmYWxzZSwKICAgICAgImVuYWJsZWQi
OiB0cnVlLAogICAgICAidmFsdWUiOiAyMDEsCiAgICAgICJsYWJlbCI6ICJwZGYiLAogICAgICAi
aGlkZGVuIjogZmFsc2UsCiAgICAgICJwcm9wZXJ0aWVzIjogbnVsbAogICAgfSwgewogICAgICAi
dXVpZCI6ICI0OWNhZTVmZC05YzA5LTQ5ODgtYTA5ZC0zNTRiNjgwY2Q5YjEiLAogICAgICAiZGVm
YXVsdCI6IGZhbHNlLAogICAgICAiZW5hYmxlZCI6IHRydWUsCiAgICAgICJ2YWx1ZSI6IDIwMiwK
ICAgICAgImxhYmVsIjogImpzb24iLAogICAgICAiaGlkZGVuIjogZmFsc2UsCiAgICAgICJwcm9w
ZXJ0aWVzIjogbnVsbAogICAgfV0KICB9XSwKICAib3ZlcnJpZGVzIjogW10sCiAgImV4cG9ydF9k
YXRlIjogMTUzMTczODc1MzIyMgp9
"""
    )