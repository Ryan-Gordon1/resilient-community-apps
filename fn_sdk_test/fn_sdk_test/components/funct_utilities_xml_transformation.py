# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_xml_transformation''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_xml_transformation")
    def _utilities_xml_transformation_function(self, event, *args, **kwargs):
        """Function: Transforms an XML document using a preexisting `xsl` stylesheet. The resulting content is returned."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_xml_transformation' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            xml_stylesheet = kwargs.get("xml_stylesheet")  # text
            xml_source = kwargs.get("xml_source")  # text

            log = logging.getLogger(__name__)
            log.info("xml_stylesheet: %s", xml_stylesheet)
            log.info("xml_source: %s", xml_source)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_xml_transformation' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
