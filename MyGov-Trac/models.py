from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime


class Site_Infos(Base):
    __tablename__ = 'gov_tracker'
    id = Column(Integer, primary_key=True)
    site_name = Column(String(100))
    region = Column(String(15))
    site_type = Column(String(25))
    site_code = Column(String(15))
    tac_name = Column(String(120))
    dt_readiness = Column(DateTime, default=datetime.utcnow)
    rfs = Column(String(5))
    rfs_date = Column(DateTime, default=datetime.utcnow)
    hu_1st_sub_date = Column(DateTime, default=datetime.utcnow)
    te_1st_resp_date = Column(DateTime, default=datetime.utcnow)
    hu_2nd_sub_date = Column(DateTime, default=datetime.utcnow)
    te_2nd_resp_date = Column(DateTime, default=datetime.utcnow)
    hu_3rd_sub_date = Column(DateTime, default=datetime.utcnow)
    te_3rd_resp_date = Column(DateTime, default=datetime.utcnow)
    accpt_date_opt = Column(DateTime, default=datetime.utcnow)
    accpt_date_plan = Column(DateTime, default=datetime.utcnow)
    signed_sites = Column(DateTime, default=datetime.utcnow)
    as_built_date = Column(DateTime, default=datetime.utcnow)
    as_build_status = Column(String(10))
    dt_status = Column(String(10))
    shr_status = Column(String(10))
    dt_planned = Column(DateTime, default=datetime.utcnow)
    integeration_status = Column(DateTime, default=datetime.utcnow)
    comnt_snags = Column(String(250))
    cluster_name = Column(String(150))
    type_stnd_alone_colcted = Column(String(150))
    instled_type_stnd_alone_colcted = Column(String(150))
    status = Column(String(100))
    pending = Column(String(120))
    pending_status = Column(String(150))
    problamatic_details = Column(String(255))
    ets_tac = Column(Integer)
    region_2 = Column(String(5))
    sf6_signed_date = Column(DateTime, default=datetime.utcnow)
    sf6_signed_comnt = Column(String(255))
    comment_history = Column(String(255))
    on_air_owner = Column(String(120))
    pp_owner = Column(String(120))
    report_comment = Column(String(150))
    hu_opt_area_owner = Column(String(120))
    planning_owner = Column(String(120))
    po_number = Column(String(25))
    trigger_date = Column(DateTime, default=datetime.utcnow)
    as_built_status2 = Column(String(120))
    r = Column(String(120))
    t = Column(String(120))

    def __init__(self, site_name=None, region=None, site_type=None, site_code=None, tac_name=None
                 , dt_readiness=None, rfs=None, rfs_date=None, hu_1st_sub_date=None, te_1st_resp_date=None, hu_2nd_sub_date=None
                 , te_2nd_resp_date=None, hu_3rd_sub_date=None, te_3rd_resp_date=None, accpt_date_opt=None, accpt_date_plan=None, signed_sites=None
                 , as_built_date=None, as_build_status=None, dt_status=None, shr_status=None, dt_planned=None, integeration_status=None
                 , comnt_snags=None, cluster_name=None, type_stnd_alone_colcted=None, instled_type_stnd_alone_colcted=None
                 , status=None, pending=None
                 , pending_status=None, problamatic_details=None, ets_tac=None, region_2=None, sf6_signed_date=None, sf6_signed_comnt=None
                 , comment_history=None, on_air_owner=None, pp_owner=None, report_comment=None, hu_opt_area_owner=None, planning_owner=None
                 , po_number=None, trigger_date=None, as_built_status2=None, r=None, t=None):
        self.site_name = site_name
        self.region = region
        self.site_type = site_type
        self.site_code = site_code
        self.tac_name = tac_name
        self.dt_readiness = dt_readiness
        self.rfs = rfs
        self.rfs_date = rfs_date
        self.hu_1st_sub_date = hu_1st_sub_date
        self.te_1st_resp_date = te_1st_resp_date
        self.hu_2nd_sub_date = hu_2nd_sub_date
        self.te_2nd_resp_date = te_2nd_resp_date
        self.hu_3rd_sub_date = hu_3rd_sub_date
        self.te_3rd_resp_date = te_3rd_resp_date
        self.accpt_date_opt = accpt_date_opt
        self.accpt_date_plan = accpt_date_plan
        self.signed_sites = signed_sites
        self.as_built_date = as_built_date
        self.as_build_status = as_build_status
        self.dt_status = dt_status
        self.shr_status = shr_status
        self.dt_planned = dt_planned
        self.integeration_status = integeration_status
        self.comnt_snags = comnt_snags
        self.cluster_name = cluster_name
        self.type_stnd_alone_colcted = type_stnd_alone_colcted
        self.instled_type_stnd_alone_colcted = instled_type_stnd_alone_colcted
        self.status = status
        self.pending = pending
        self.pending_status = pending_status
        self.problamatic_details = problamatic_details
        self.ets_tac = ets_tac
        self.region_2 = region_2
        self.sf6_signed_date = sf6_signed_date
        self.sf6_signed_comnt = sf6_signed_comnt
        self.comment_history = comment_history
        self.on_air_owner = on_air_owner
        self.pp_owner = pp_owner
        self.report_comment = report_comment
        self.hu_opt_area_owner = hu_opt_area_owner
        self.planning_owner = planning_owner
        self.po_number = po_number
        self.trigger_date = trigger_date
        self.as_built_status2 = as_built_status2
        self.r = r
        self.t = t

    def __repr__(self):
        return '<Site_Infos %r>' % (self.site_code)
