using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BYS.Entity.Entities
{
    public class StudentCourse
    {

        public int StudentId { get; set; } // Composite Key Part 1
        public Student Student { get; set; }
        //StudentCourse nesnesinden bu kaydın hangi öğrenciye-le ilişkili olduğunu öğrenmek için

        public int CourseId { get; set; } // Composite Key Part 2
        public Course Course { get; set; }
        //StudentCourse nesnesinden bu kaydın hangi ders ile ilişkili olduğunu öğrenmek için
    }
}
