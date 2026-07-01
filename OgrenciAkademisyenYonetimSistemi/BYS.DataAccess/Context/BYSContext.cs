using BYS.Entity.Entities;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BYS.DataAccess.Context
{
    public class BYSContext : DbContext
    {
        public BYSContext(DbContextOptions options): base(options) { }

        public DbSet<Student> Students { get; set; }    
        public DbSet<Instructor> Instructors { get; set; }    
        public DbSet<Course> Courses { get; set; }    
        public DbSet<StudentCourse> StudentCourses { get; set; }


        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // StudentCourse için Composite Key tanımlama
            modelBuilder.Entity<StudentCourse>()
                .HasKey(sc => new { sc.StudentId, sc.CourseId });

            // Diğer yapılandırmalar yapılabilir
            base.OnModelCreating(modelBuilder);
        }

    }
}
