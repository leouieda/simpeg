# Copyright (c) 2013 SimPEG Developers.
# Distributed under the terms of the MIT License.
# SPDX-License-Identifier: MIT
# This code is part of the SimPEG project (https://simpeg.xyz)
from .static_utils import (
    electrode_separations,
    source_receiver_midpoints,
    geometric_factor,
    apparent_resistivity,
    plot_pseudosection,
    plot_pseudoSection,
    gen_DCIPsurvey,
    generate_dcip_survey,
    generate_dcip_survey_line,
    writeUBC_DCobs,
    writeUBC_DClocs,
    convertObs_DC3D_to_2D,
    readUBC_DC2Dpre,
    readUBC_DC3Dobs,
    xy_2_lineID,
    r_unit,
    getSrc_locs,
    gettopoCC,
    drapeTopotoLoc,
    genTopography,
    closestPointsGrid,
    gen_3d_survey_from_2d_lines,
    plot_layer,
)
