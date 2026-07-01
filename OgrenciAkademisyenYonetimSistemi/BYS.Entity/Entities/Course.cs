using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BYS.Entity.Entities
{
    public class Course
    {

        public int CourseId { get; set; } // Primary Key
        public string CourseName { get; set; }
        public int Credits { get; set; }

        // bu dersi hangi öğrentmen veriyor 
        public int InstructorId { get; set; } // Foreign Key
        public Instructor Instructor { get; set; }
        //ders nesnesinden öğretmen nesnesine navigasyon sağlar. Bi dersin hangi akademisyen tarafından 
        //verildiğini öğrenmek için bu alan kullanılır

        // bu dersi alan öğrencilerin listesi
        public ICollection<Student> Students { get; set; }
    }
}
