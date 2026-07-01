using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BYS.Entity.Entities
{
    public class Student
    {
        public int StudentId { get; set; } // Primary Key
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
       

        // Bu alan bir öğrencinin seçtiği dersleri listelemek için kullanılır 
        public ICollection<Course> CoursesSelected { get; set; }

    }
}
