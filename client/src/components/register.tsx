import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import { Input } from "./ui/input";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form";

export default function Register() {
  
    const form = useForm({
      defaultValues: {
        name: "",
        lastName: "",
        password: "",
        email: "",
        confirmPassword: "",
      },
    });
  
    const onSubmit = (data) => {
      console.log("Datos del formulario:", data);
    };
  
    return( 
  <>
    <h1>Register</h1>
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4 p-6 bg-white rounded-md shadow-md flex flex-col items-center">
        
      <div className="flex space-x-4 ">
     <FormField
        control={form.control} 
          name="name"
          rules = {{
            required: "The name is required"
          }}    
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Nombre</FormLabel>
              <FormControl>
                <Input placeholder="Enter your name" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
        )}
        />

        <FormField
        control={form.control} 
          name="lastName"
          rules = {{
            required: "The last name is required"
          }}          
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Apellido</FormLabel>
              <FormControl>
                <Input placeholder="Enter your last name" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
        )}
        />
 
      </div>
    
      <div className="flex space-x-4">
    <FormField
        control={form.control} 
          name="password"
          rules = {{
            required: "The password is required",
            minLength: {
                value: 6,
                message: "the password must have at least 6 characters",
              },
          }}
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Contraseña</FormLabel>
              <FormControl>
                <Input type="password" placeholder="Enter your password" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
        )}
        />
          
        <FormField
        control={form.control} 
          name="confirmPassword"
          rules = {{
            required: "Confirm password is required",
            validate: (value) =>
              value === form.getValues("password") || "Passwords do not match",
          }}
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Confirm Password</FormLabel>
              <FormControl>
                <Input type="password" placeholder="Confirm your password" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
        )}
        />
      </div>
        
        <FormField
        control={form.control}
          name="email"
          rules = {{
            required: "Email is required",
            pattern: {
                value: /^[^@ ]+@[^@ ]+\.[^@ .]{2,}$/,
                message: "Email is not valid",
              },
          }}        
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input type="email" placeholder="Enter your email" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
        )}
        />
        <Button className="mt-6" type="submit">Register</Button>
      </form>
    </Form>  
    </>
    )
  }