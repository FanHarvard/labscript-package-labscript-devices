#####################################################################
#                                                                   #
# /NI_DAQmx/models/_subclass_template.py                            #
#                                                                   #
# Copyright 2018, Christopher Billington                            #
#                                                                   #
# This file is part of the module labscript_devices, in the         #
# labscript suite (see http://labscriptsuite.org), and is           #
# licensed under the Simplified BSD License. See the license.txt    #
# file in the root of the project for the full license.             #
#                                                                   #
#####################################################################

#####################################################################
#     WARNING                                                       #
#                                                                   #
# This file is auto-generated, any modifications may be             #
# overwritten. See README.txt in this folder for details            #
#                                                                   #
#####################################################################


from labscript_devices.NI_DAQmx.labscript_devices import NI_DAQmx

#:
CAPABILITIES = {
    'AI_range': [-10.0, 10.0],
    'AI_range_Diff': [-10.0, 10.0],
    'AI_start_delay': 4e-08,
    'AI_term': 'RSE',
    'AI_term_cfg': {
        'ai0': ['RSE', 'NRSE', 'Diff'],
        'ai1': ['RSE', 'NRSE', 'Diff'],
        'ai10': ['RSE', 'NRSE'],
        'ai11': ['RSE', 'NRSE'],
        'ai12': ['RSE', 'NRSE'],
        'ai13': ['RSE', 'NRSE'],
        'ai14': ['RSE', 'NRSE'],
        'ai15': ['RSE', 'NRSE'],
        'ai16': ['RSE', 'NRSE', 'Diff'],
        'ai17': ['RSE', 'NRSE', 'Diff'],
        'ai18': ['RSE', 'NRSE', 'Diff'],
        'ai19': ['RSE', 'NRSE', 'Diff'],
        'ai2': ['RSE', 'NRSE', 'Diff'],
        'ai20': ['RSE', 'NRSE', 'Diff'],
        'ai21': ['RSE', 'NRSE', 'Diff'],
        'ai22': ['RSE', 'NRSE', 'Diff'],
        'ai23': ['RSE', 'NRSE', 'Diff'],
        'ai24': ['RSE', 'NRSE'],
        'ai25': ['RSE', 'NRSE'],
        'ai26': ['RSE', 'NRSE'],
        'ai27': ['RSE', 'NRSE'],
        'ai28': ['RSE', 'NRSE'],
        'ai29': ['RSE', 'NRSE'],
        'ai3': ['RSE', 'NRSE', 'Diff'],
        'ai30': ['RSE', 'NRSE'],
        'ai31': ['RSE', 'NRSE'],
        'ai4': ['RSE', 'NRSE', 'Diff'],
        'ai5': ['RSE', 'NRSE', 'Diff'],
        'ai6': ['RSE', 'NRSE', 'Diff'],
        'ai7': ['RSE', 'NRSE', 'Diff'],
        'ai8': ['RSE', 'NRSE'],
        'ai9': ['RSE', 'NRSE'],
    },
    'AO_range': [-10.0, 10.0],
    'max_AI_multi_chan_rate': 1000000.0,
    'max_AI_single_chan_rate': 1000000.0,
    'max_AO_sample_rate': 250000.0,
    'max_DO_sample_rate': 10000000.0,
    'min_semiperiod_measurement': 1e-07,
    'num_AI': 32,
    'num_AO': 4,
    'num_CI': 4,
    'ports': {'port0': {'num_lines': 16, 'supports_buffered': True}},
    'PFI_connections': {
        'PFI0': 'port0/line0',
        'PFI1': 'port0/line1',
        'PFI2': 'port0/line2',
        'PFI3': 'port0/line3',
        'PFI4': 'port0/line4',
        'PFI5': 'port0/line5',
        'PFI6': 'port0/line6',
        'PFI7': 'port0/line7',
        'PFI8': 'port0/line8',
        'PFI9': 'port0/line9',
        'PFI10': 'port0/line10',
        'PFI11': 'port0/line11',
        'PFI12': 'port0/line12',
        'PFI13': 'port0/line13',
        'PFI14': 'port0/line14',
        'PFI15': 'port0/line15',
    },
    'supports_buffered_AO': True,
    'supports_buffered_DO': True,
    'supports_semiperiod_measurement': True,
    'supports_simultaneous_AI_sampling': True,
}


class NI_USB_6453(NI_DAQmx):
    description = 'NI-USB-6453'

    def __init__(self, *args, **kwargs):
        """Class for NI-USB-6453"""
        # Any provided kwargs take precedent over capabilities
        combined_kwargs = CAPABILITIES.copy()
        combined_kwargs.update(kwargs)
        NI_DAQmx.__init__(self, *args, **combined_kwargs)
