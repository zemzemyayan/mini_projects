using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BYS.Entity.Entities
{
    public class Instructor
    {
        public int InstructorId { get; set; } // Primary Key
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public string Department { get; set; }

        //bu alan bir akademisyenin verdiği dersleri listelemek için kullanılır 
        public ICollection<Course> Courses { get; set; }

    }
}
