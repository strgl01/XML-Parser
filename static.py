
DATA={
'DATE FILED' : [],
'TAX PERIOD':[],
'PREPARER EIN':[],
'PREPAREER':[],
'FORM':[],
'EIN':[],
'COMPANY NAME':[],
'ADDRESS':[],
'CITY':[],
'STATE':[],
'ZIP CODE':[],
'PREPAREER NAME':[],
'GROSS RECEIPTS':[],
'WEB DOMAIN=':[],
'DATE FOUNDED':[],
'MISSION STATEMENT':[],
'NUMBER OF EMPLOYEES':[],
'NUMBER OF VOLUNTEERS':[],
'LAST YEAR TOTAL REVENUE':[],
'THIS YEAR TOTAL REVENUE':[],
'LAST YEAR TOTAL SALARIES AND BENEFITS':[],
'THIS YEAR TOTAL SALARIES AND BENEFITS':[],
'LAST YEAR TOTAL EXPENSES':[],
'THIS YEAR TOTAL EXPENSES':[],
'LAST YEAR NET REVENUE':[],
'THIS YEAR NET REVENUE':[],
'LAST YEAR TOTAL ASSETS':[],
'THIS YEAR TOTAL ASSETS':[],
'LAST YEAR TOTAL LIABILITIES':[],
'THIS YEAR TOTAL LIABILITIES':[],
'LAST YEAR TOTAL NET ASSETS':[],
'THIS YEAR TOTAL NET ASSETS':[],
'HIGHLY COMPENSATED EE':[],
'EMPLOYEE BENEFITS TOTAL':[],
'PAYROLL TAXES':[],
'Total Revenue':[]  ,
'PENSION PLAN AND 401K':[],
'EMPLOYEE BENEFITS':[],
'PAYROLL TAXES1':[],
'ADVERTISING':[],
'OFFICE EXPENSE':[],
'INFORMATION TECHNOLOGY':[],
'OCCUPANCY':[],
'TRAVEL':[],
'CONFERENCES':[],
'INTEREST':[],
'INSURANCE':[],
'LAST YEAR CASH':[],
'THIS YEAR CASH':[],
'LAST YEAR SAVINGS':[],
'THIS YEAR SAVINGS':[],
'LAST YEAR AR':[],
'THIS YEAR AR':[],
'LAST YEAR ASSETS':[],
'THIS YEAR ASSETS':[],
'LAST YEAR LIABILITIES':[],
'THIS YEAR LIABILITIES':[],
'LAST YEAR NET ASSETS':[],
'THIS YEAR NET ASSETS':[],
'OFFICER COMPENSATION':[],
'EE WAGES':[],
}

attr_chain=[
     'ReturnHeader.ReturnTs.text'
    ,'ReturnHeader.TaxPeriodEndDt.text'
    ,'ReturnHeader.PreparerFirmGrp.PreparerFirmEIN.text'
    ,'ReturnHeader.PreparerFirmGrp.PreparerFirmName.BusinessNameLine1Txt.text'
    ,'ReturnHeader.ReturnTypeCd.text'
    ,'ReturnHeader.Filer.EIN.text'
    ,'ReturnHeader.Filer.BusinessName.BusinessNameLine1Txt.text'
    ,'ReturnHeader.Filer.USAddress.AddressLine1Txt.text'
    ,'ReturnHeader.Filer.USAddress.CityNm.text'
    ,'ReturnHeader.Filer.USAddress.StateAbbreviationCd.text'
    ,'ReturnHeader.Filer.USAddress.ZIPCd.text'
    ,'ReturnHeader.PreparerPersonGrp.PreparerPersonNm.text'
    ,'ReturnData.IRS990.GrossReceiptsAmt.text'
    ,'ReturnData.IRS990.WebsiteAddressTxt.text'
    ,'ReturnData.IRS990.FormationYr.text'
    ,'ReturnData.IRS990.ActivityOrMissionDesc.text'
    ,'ReturnData.IRS990.TotalEmployeeCnt.text'
    ,'ReturnData.IRS990.TotalVolunteersCnt.text'
    ,'ReturnData.IRS990.PYTotalRevenueAmt.text'
    ,'ReturnData.IRS990.CYTotalRevenueAmt.text'
    ,'ReturnData.IRS990.PYSalariesCompEmpBnftPaidAmt.text'
    ,'ReturnData.IRS990.CYSalariesCompEmpBnftPaidAmt.text'
    ,'ReturnData.IRS990.PYTotalExpensesAmt.text'
    ,'ReturnData.IRS990.CYTotalExpensesAmt.text'
    ,'ReturnData.IRS990.PYRevenuesLessExpensesAmt.text'
    ,'ReturnData.IRS990.CYRevenuesLessExpensesAmt.text'
    ,'ReturnData.IRS990.TotalAssetsBOYAmt.text'
    ,'ReturnData.IRS990.TotalAssetsEOYAmt.text'
    ,'ReturnData.IRS990.TotalLiabilitiesBOYAmt.text'
    ,'ReturnData.IRS990.TotalLiabilitiesEOYAmt.text'
    ,'ReturnData.IRS990.NetAssetsOrFundBalancesBOYAmt.text'
    ,'ReturnData.IRS990.NetAssetsOrFundBalancesEOYAmt.text'
    ,'ReturnData.IRS990.IndivRcvdGreaterThan100KCnt.text'
    ,'ReturnData.IRS990.OtherEmployeeBenefitsGrp.TotalAmt.text'
    ,'ReturnData.IRS990.PayrollTaxesGrp.TotalAmt.text'
    ,'ReturnData.IRS990.TotalRevenueGrp.TotalRevenueColumnAmt.text'
    ,'ReturnData.IRS990.PensionPlanContributionsGrp.TotalAmt.text'
    ,'ReturnData.IRS990.OtherEmployeeBenefitsGrp.TotalAmt.text'
    ,'ReturnData.IRS990.PayrollTaxesGrp.TotalAmt.text'
    ,'ReturnData.IRS990.AdvertisingGrp.TotalAmt.text'
    ,'ReturnData.IRS990.OfficeExpensesGrp.TotalAmt.text'
    ,'ReturnData.IRS990.InformationTechnologyGrp.TotalAmt.text'
    ,'ReturnData.IRS990.OccupancyGrp.TotalAmt.text'
    ,'ReturnData.IRS990.TravelGrp.TotalAmt.text'
    ,'ReturnData.IRS990.ConferencesMeetingsGrp.TotalAmt.text'
    ,'ReturnData.IRS990.DepreciationDepletionGrp.TotalAmt.text'
    ,'ReturnData.IRS990.InsuranceGrp.TotalAmt.text'
    ,'ReturnData.IRS990.SavingsAndTempCashInvstGrp.BOYAmt.text'
    ,'ReturnData.IRS990.SavingsAndTempCashInvstGrp.EOYAmt.text'
    ,'ReturnData.IRS990.PledgesAndGrantsReceivableGrp.BOYAmt.text'
    ,'ReturnData.IRS990.PledgesAndGrantsReceivableGrp.EOYAmt.text'
    ,'ReturnData.IRS990.AccountsReceivableGrp.BOYAmt.text'
    ,'ReturnData.IRS990.AccountsReceivableGrp.EOYAmt.text'
    ,'ReturnData.IRS990.TotalAssetsGrp.BOYAmt.text'
    ,'ReturnData.IRS990.TotalAssetsGrp.EOYAmt.text'
    ,'ReturnData.IRS990.TotalLiabilitiesGrp.BOYAmt.text'
    ,'ReturnData.IRS990.TotalLiabilitiesGrp.EOYAmt.text'
    ,'ReturnData.IRS990.NoDonorRestrictionNetAssetsGrp.BOYAmt.text'
    ,'ReturnData.IRS990.NoDonorRestrictionNetAssetsGrp.EOYAmt.text'
    ,'ReturnData.IRS990.CompCurrentOfcrDirectorsGrp.TotalAmt.text'
    ,'ReturnData.IRS990.OtherSalariesAndWagesGrp.TotalAmt.text'
]




