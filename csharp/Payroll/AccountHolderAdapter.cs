using Payroll.ThirdParty;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Payroll {
    internal class AccountHolderAdapter : AccountHolder {
        private readonly Employable employable;

        public AccountHolderAdapter(Employable employable)
        {
            this.employable = employable;
        }

        public string GetAccountDetails()
        {
            return employable.GetNote("AccountDetails");
        }
    }
}
