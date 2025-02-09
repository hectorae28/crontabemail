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

export default function Login() {
  
    const form = useForm({
      defaultValues: {
        password: "",
        email: "",
      },
    });
  
  
    const onSubmit = (data) => {
      console.log("Datos del formulario:", data);
    };
  
    return( 
      <>
        <h1>Inicio de sesión</h1>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4 p-6 bg-white rounded-md shadow-md flex flex-col items-center">
          <FormField
          control={form.control} 
          name="email"
          rules = {{
            required: "El email es requerido"
          }} 
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input placeholder="Ingresa tu email" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
          )}
        />
          <FormField
          control={form.control}
          name="password"
          rules = {{
            required: "La contarseña es requerida"
          }}          
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Password</FormLabel>
              <FormControl>
                <Input placeholder="Ingresa tu contraseña" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
          )}
        />
        <Button type="submit" className="mt-6">Iniciar sesión</Button>
      </form>
    </Form>  
      </>
    )
  }